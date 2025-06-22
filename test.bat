@echo off
REM 디렉토리 생성
mkdir ray_platform\src\api
mkdir ray_platform\src\datasource
mkdir ray_platform\src\jobs
mkdir ray_platform\src\scheme\kafka
mkdir ray_platform\src\scheme\mongodbs
mkdir ray_platform\src\scheme\oracles
mkdir ray_platform\src\scheme\redis
mkdir ray_platform\src\users
mkdir ray_platform\src\websocket
mkdir ray_platform\tests

REM 파일 생성 (type nul > filename)
type nul > ray_platform\src\api\kafkasample.py
type nul > ray_platform\src\api\mongodbsample.py
type nul > ray_platform\src\api\oraclesample.py
type nul > ray_platform\src\api\redissample.py

type nul > ray_platform\src\datasource\loadkafka.py
type nul > ray_platform\src\datasource\loadmongodb.py
type nul > ray_platform\src\datasource\loadoracle.py
type nul > ray_platform\src\datasource\loadredis.py
type nul > ray_platform\src\datasource\loadrediscluster.py

type nul > ray_platform\src\jobs\cronjob.py
type nul > ray_platform\src\jobs\intervaljob.py

type nul > ray_platform\src\users\config.py
type nul > ray_platform\src\users\constants.py
type nul > ray_platform\src\users\dependencies.py
type nul > ray_platform\src\users\exceptions.py
type nul > ray_platform\src\users\models.py
type nul > ray_platform\src\users\router.py
type nul > ray_platform\src\users\schemas.py
type nul > ray_platform\src\users\service.py
type nul > ray_platform\src\users\utils.py

type nul > ray_platform\src\websocket\chat_broker.py
type nul > ray_platform\src\websocket\chat.py

type nul > ray_platform\src\config.py
type nul > ray_platform\src\exceptions.py
type nul > ray_platform\src\models.py
type nul > ray_platform\src\router.py
type nul > ray_platform\src\server.py

type nul > ray_platform\app.py
type nul > ray_platform\config.dev.yml
type nul > ray_platform\config.tml
type nul > ray_platform\logger.yml
type nul > ray_platform\requirements.txt

echo 디렉토리 및 파일 생성 완료!
pause
