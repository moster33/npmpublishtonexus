# npmpublishtonexus
本地node_modules批量publish到私服

## 背景
```
内网网络隔离，自己搭建了私服，需要将vue开发依赖的包都传到内网私服
实际操作过程中，会有部分失败，因此写了python脚本，批量进行上传
```

- 使用时，需要将本地的npm仓库配置为私服仓库，并进行login
```
npm config set registry=xxxx
npm login
```
- 准备完成后，将upload.py放到项目node_modules目录下，执行如下命令
```
python upload.py
```
