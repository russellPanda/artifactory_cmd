# artifactory_cmd
artifactory命令行工具



1. 依赖

   ```
   Click==7.0
   pyartifactory==1.9.1
   ```

2. 使用

   ```shell
   russell@:arti$ python3 testClick.py --help
   Usage: testClick.py [OPTIONS] COMMAND [ARGS]...
   
   Options:
     -f, --file TEXT  config file
     --help           Show this message and exit.
   
   Commands:
     artifact
     repo
   russell@:arti$ python3 testClick.py repo --help
   Usage: testClick.py repo [OPTIONS] COMMAND [ARGS]...
   
   Options:
     --help  Show this message and exit.
   
   Commands:
     create  create repo
     delete  delete repo
     info    info repo
     list    list repo
   russell@:arti$ python3 testClick.py repo create --help
   Usage: testClick.py repo create [OPTIONS] NAME
   
     create [repo name]
   
   Options:
     --name TEXT  repo to create
     --help       Show this message and exit.
   
   ```

3. 待解决

   - [ ]  -f file 参数放置命令最后
   - [ ] read_config 函数待补充,默认读`config.yml`

