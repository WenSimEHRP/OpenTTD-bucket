# OpenTTD-Bucket

[![Tests](https://github.com/WenSimEHRP/OpenTTD-Buckets/actions/workflows/ci.yml/badge.svg)](https://github.com/WenSimEHRP/OpenTTD-Buckets/actions/workflows/ci.yml) [![Excavator](https://github.com/WenSimEHRP/OpenTTD-Buckets/actions/workflows/excavator.yml/badge.svg)](https://github.com/WenSimEHRP/OpenTTD-Buckets/actions/workflows/excavator.yml)

This is a bucket created for [Scoop](https://scoop.sh). This bucket contains manifests of various versions of OpenTTD, including patched and legacy versions, and a handful of OpenTTD related tools.

## Mirror | 镜像

Gitee: https://gitee.com/wensimehrp/OpenTTD-bucket

Please note that the mirror may not be the latest version.\
请注意镜像可能不是最新版本。

## Installing

To install an application, simply open Powershell and run the following commands:

```ps
# add bucket
scoop bucket add openttd-bucket https://github.com/WenSimEHRP/OpenTTD-bucket

# install applications, say openttd-nightly
scoop install openttd-bucket/openttd-nightly
# or
scoop install openttd-nightly
```

## Application List

| Name            | Description                                              | Homepage                                               |
|-----------------|----------------------------------------------------------|--------------------------------------------------------|
| OpenTTD         | The OpenTTD game                                         | https://www.openttd.org                                |
| OpenTTD-JGRPP   | OpenTTD JGR's Patch Pack                                 | https://github.com/jgrennison/openttd-patches          |
| OpenTTD-Nightly | OpenTTD Nightly Version                                  | https://www.openttd.org                                |
| OpenTTD-CM      | CityMania Patched Client                                 | https://github.com/citymania-org/cmclient              |
| nml             | Powerful GRF compiler                                    | https://github.com/openttd/grfcodec                    |
| grfcodec        | GRF compiler and decompiler                              | https://github.com/openttd/nml                         |
| yagl            | GRF compiler and decompiler with better formatted output | https://github.com/unicyclebloke/yagl                  |
| linkgrf         | GRF linking application for use with m4nfo               | http://www.ttdpatch.de/grfspecs/m4nfoManual/index.html |
| spotvox         | Voxel renderer written in Java                           | https://github.com/tommyettinger/spotvox               |
| GoRender        | Feature-rich voxel renderer written in GO                | https://github.com/mattkimber/gorender                 |
| grf2html        | Deprecated GRF document generator                        | https://github.com/frosch123/grf2html                  |
| grfmaker        | Deprecated graphical GRF Maker                           | https://users.tt-forums.net/grfmaker                   |
