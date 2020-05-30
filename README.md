# vstNN

Using the dataset provided by https://www.idmt.fraunhofer.de/en/business_units/m2d/smt/guitar.html

MrsWatson can be retrieved from https://github.com/teragonaudio/MrsWatson

And the effects vst plugins can be downloaded from various places. The one being used in this project comes from [DistorqueAudio Face Bender](http://distorqueaudio.com/plugins/face-bender.html).

_THIS IS A WIP_

Dataset Processor

The parallel approach significantly increases the performance by almost an order of magnitude. The following benchmark shows the difference between the parallel approach verses serial. The dataset contained 78 wav file. Point to note here is that the following results come from single run timings and I've seen that averaging the run time of parallel runs brings the number down quite significantly.

#### Parallel
```
PS D:\Code\WaveNetVA> Measure-Command {python dataset-parallel.py -i "data\IDMT-SMT-GUITAR_V2\dataset1\Fender Strat Clean Neck SC\audio" -o test\dataset1 -p "Face Bender x64" -r "plugins\Distorque Face Bender x64\custom.fxp"}


Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 4
Milliseconds      : 802
Ticks             : 48021122
TotalDays         : 5.55800023148148E-05
TotalHours        : 0.00133392005555556
TotalMinutes      : 0.0800352033333333
TotalSeconds      : 4.8021122
TotalMilliseconds : 4802.1122
```

#### Serial
```
PS D:\Code\WaveNetVA> Measure-Command {python dataset.py -i "data\IDMT-SMT-GUITAR_V2\dataset1\Fender Strat Clean Neck SC\audio" -o test\dataset1 -p "Face Bender x64" -r "plugins\Distorque Face Bender x64\custom.fxp"}


Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 28
Milliseconds      : 304
Ticks             : 283046973
TotalDays         : 0.000327600663194444
TotalHours        : 0.00786241591666667
TotalMinutes      : 0.471744955
TotalSeconds      : 28.3046973
TotalMilliseconds : 28304.6973
```