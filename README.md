# pose_estimation
[원본 깃허브 링크](https://github.com/itzThillaiC/AI-Fitness-trainer)

```py
python main.py -t pull-up -vs videos/pull-up.mp4
```
videos파일에있는 pull-up.mp4 포즈 탐지

```py
python main.py -t push-up -vs videos/push-up.mp4
```
videos파일에있는 push-up.mp4 포즈 탐지

```py
python main.py -t sit-up -vs videos/sit-up.mp4
```
videos파일에있는 sit-up.mp4 포즈 탐지

```py
python main.py -t squat -vs videos/squat.mp4
```
videos파일에있는 squat.mp4 포즈 탐지

만약 자신이 측정하고 싶다면 -vs를 빼고 -t 태그에 운동종류를 입력
```py
python main.py -t sit-up
python main.py -t pull-up
python main.py -t push-up
python main.py -t squat
```

포즈 측정을 종료하고 싶다면 키보드 **q** 입력 
