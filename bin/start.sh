#!/usr/bin/env bash

cd `dirname $0`
cd ..

base_dir=`pwd`
tmp_dir=${base_dir}/tmp
pid_file_path=${tmp_dir}/model-serving-demo.pid
log_file_path=${tmp_dir}/model-serving-demo.log

bind_host=0.0.0.0
bind_port=9999
workers=2

nohup gunicorn -b ${bind_host}:${bind_port} -w ${workers} -p ${pid_file_path} main:app > ${log_file_path} 2>&1 &
