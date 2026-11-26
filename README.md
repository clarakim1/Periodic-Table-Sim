# Interactive 3D Periodic Table & Chemistry Experiment Simulator

학생들이 실제로 수행한 실험(마그네슘-공기 전지, 물·황산구리 전기분해, 탄산칼슘 침전, 화산, 비타민 C–아이오딘, 불꽃 반응 등)에 쓰인 원소 17종을 3D 주기율표로 연결한 프로젝트입니다.

## 구성

```
periodic-table-sim/
├─ index.html                       # 3D 시뮬레이션 웹뷰어 (더블클릭으로 열기)
├─ three.min.js                     # three.js r128 (오프라인 실행용, MIT)
├─ fusion360/periodic_table.py      # Fusion 360 스크립트: 원소 타일 17개 생성
├─ makerworld/LISTING.md            # MakerWorld 업로드 문안
└─ README.md
```

## 사용법

1. **웹 시뮬레이션**: `index.html`을 브라우저로 엽니다(인터넷 불필요). 블록 클릭 → 원자량·전자배치·관련 실험·화합물·반응식.
2. **Fusion 360**: 유틸리티 → 스크립트 및 추가 기능 → 스크립트 `+` → `fusion360` 폴더 추가 → 실행. 타일 20×20×4 mm, 글자 0.6 mm 돌출.
3. **출력용 내보내기**: 파일 → 내보내기 → 3MF.

## GitHub에 올리기

```bash
git init && git add . && git commit -m "Initial: 3D periodic table simulator"
git branch -M main
git remote add origin https://github.com/<아이디>/periodic-table-sim.git
git push -u origin main
```
저장소 Settings → Pages에서 `main` / `/ (root)`를 선택하면 시뮬레이션이 링크로 공개됩니다.

## 확인이 필요한 항목

- Li, Sr, Ba는 실제 불꽃 실험 시료 확인이 필요합니다.
- 황산, 염산, 황산아연, 포도당의 실제 사용 여부는 별도 확인이 필요합니다.
- Zn(아연)은 사용 기록이 없어 제외했습니다.
- 페리시안화칼륨 + 홍차의 색 변화 반응식은 확정하지 않았습니다.

---
