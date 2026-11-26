"""Fusion 360 스크립트: 실험 원소 17종 주기율표 타일 생성.
실행: Fusion 360 > 유틸리티 > 추가 기능 > 스크립트 및 추가 기능 > 스크립트 > + 로 이 파일의 폴더 추가 > 실행
단위: Fusion API는 cm 사용 (1.0 = 10 mm). 타일 20x20x4 mm, 글자 돌출 0.6 mm.
※ 아직 실제 Fusion에서 검증되지 않은 초안입니다. 글자 API에서 오류가 나면 알려주세요.
"""
import adsk.core, adsk.fusion, traceback

# (원자번호, 기호, 주기, 족)
ELEMENTS = [
    (1, 'H', 1, 1), (3, 'Li', 2, 1), (6, 'C', 2, 14), (7, 'N', 2, 15), (8, 'O', 2, 16),
    (11, 'Na', 3, 1), (12, 'Mg', 3, 2), (16, 'S', 3, 16), (17, 'Cl', 3, 17),
    (19, 'K', 4, 1), (20, 'Ca', 4, 2), (26, 'Fe', 4, 8), (29, 'Cu', 4, 11), (35, 'Br', 4, 17),
    (38, 'Sr', 5, 2), (53, 'I', 5, 17), (56, 'Ba', 6, 2),
]
TILE, THICK, TEXT_H, PITCH = 2.0, 0.4, 0.06, 2.2   # cm


def add_text(comp, plane, text, height, cx, cy, width):
    sk = comp.sketches.add(plane)
    inp = sk.sketchTexts.createInput2(text, height)
    inp.setAsMultiLine(
        adsk.core.Point3D.create(cx - width / 2, cy + height, 0),
        adsk.core.Point3D.create(cx + width / 2, cy - height, 0),
        adsk.core.HorizontalAlignments.CenterHorizontalAlignment,
        adsk.core.VerticalAlignments.MiddleVerticalAlignment, 0)
    return sk.sketchTexts.add(inp)


def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = adsk.fusion.Design.cast(app.activeProduct)
        root = design.rootComponent
        for z, sym, p, g in ELEMENTS:
            occ = root.occurrences.addNewComponent(adsk.core.Matrix3D.create())
            comp = occ.component
            comp.name = f'{z:03d}_{sym}'
            x, y = (g - 1) * PITCH, -(p - 1) * PITCH

            # 타일 본체
            sk = comp.sketches.add(comp.xYConstructionPlane)
            sk.sketchCurves.sketchLines.addTwoPointRectangle(
                adsk.core.Point3D.create(x, y, 0),
                adsk.core.Point3D.create(x + TILE, y + TILE, 0))
            ext = comp.features.extrudeFeatures
            body = ext.addSimple(sk.profiles.item(0), adsk.core.ValueInput.createByReal(THICK),
                                 adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

            # 윗면 높이에 평면을 만들고 글자 스케치
            pi = comp.constructionPlanes.createInput()
            pi.setByOffset(comp.xYConstructionPlane, adsk.core.ValueInput.createByReal(THICK))
            top = comp.constructionPlanes.add(pi)
            cx, cy = x + TILE / 2, y + TILE / 2
            t1 = add_text(comp, top, sym, 0.8, cx, cy, TILE)
            t2 = add_text(comp, top, str(z), 0.3, x + 0.35, y + TILE - 0.3, 0.5)
            for t in (t1, t2):
                ei = ext.createInput(t, adsk.fusion.FeatureOperations.JoinFeatureOperation)
                ei.setDistanceExtent(False, adsk.core.ValueInput.createByReal(TEXT_H))
                ext.add(ei)
        ui.messageBox('완료: 17개 원소 타일을 만들었습니다.\n파일 > 내보내기에서 3MF로 저장하세요.')
    except Exception:
        if ui:
            ui.messageBox('오류:\n{}'.format(traceback.format_exc()))
