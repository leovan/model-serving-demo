#!/usr/bin/env bash

cd `dirname $0`
cd ..

base_dir=`pwd`
tmp_dir=${base_dir}/tmp
pid_file_path=${tmp_dir}/model-serving-demo.pid

kill -TERM `echo ${pid_file_path}`
