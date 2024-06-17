# OpenTTD-Bucket

[![Tests](https://github.com/WenSimEHRP/OpenTTD-Buckets/actions/workflows/ci.yml/badge.svg)](https://github.com/WenSimEHRP/OpenTTD-Buckets/actions/workflows/ci.yml) [![Excavator](https://github.com/WenSimEHRP/OpenTTD-Buckets/actions/workflows/excavator.yml/badge.svg)](https://github.com/WenSimEHRP/OpenTTD-Buckets/actions/workflows/excavator.yml)

This is a bucket created for [Scoop](https://scoop.sh). This bucket contains manifests of various versions of OpenTTD, including patched and legacy versions, and a handful of OpenTTD related tools.

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
