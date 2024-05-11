# OpenTTD-Buckets

[![Tests](https://github.com/WenSimEHRP/OpenTTD-Buckets/actions/workflows/ci.yml/badge.svg)](https://github.com/WenSimEHRP/OpenTTD-Buckets/actions/workflows/ci.yml) [![Excavator](https://github.com/WenSimEHRP/OpenTTD-Buckets/actions/workflows/excavator.yml/badge.svg)](https://github.com/WenSimEHRP/OpenTTD-Buckets/actions/workflows/excavator.yml)

This is a bucket created for [Scoop](https://scoop.sh). This bucket will contain various versions of OpenTTD, allowing users to choose and download as per their needs.


## How do I install these manifests?

After manifests have been committed and pushed, run the following:

```pwsh
scoop bucket add OpenTTD-Buckets https://github.com/WenSimEHRP/OpenTTD-Buckets
scoop install OpenTTD-Buckets/<manifestname>
```
