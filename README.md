# aws-pragmatic
pragmatic aws

## check docker status
sudo systemctl status docker

docker HW0giCUUyJ3QVpk<SZnN

fn init --runtime python hello-python
fn list context
fn create context loony-compartment --provider oracle
fn use context loony-compartment
fn update context oracle.compartment-id ocid1.compartment.oc1..aaaaaaaa2i7dnm62erlyjka3e5oxyp3cnf4tkg62j2oqr6oz6dy4qtn325nq

fn update context api-url https://functions.ap-mumbai-1.oraclecloud.com

fn update context registry bom.ocir.io/bm8d4e9ri4v2/loonyimg

docker login -u 'bm8d4e9ri4v2/arun.siv81@gmail.com' bom.ocir.io

fn deploy --app pythonapp

fn invoke pythonapp my-func