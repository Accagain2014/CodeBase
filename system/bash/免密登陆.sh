# 简易版本, 有时还需修改权限

get_hostname()
{
    echo ***${1}***
}

host_start=19
host_end=30

for ((i=${host_start}; i<=${host_end}; i++))
do
    hostname=`get_hostname ${i}`
	scp ~/.ssh/id_rsa.pub ${hostname}:~/
	ssh $hostname "mkdir ~/.ssh; cat ~/id_rsa.pub >> ~/.ssh/authorized_keys ; rm ~/id_rsa.pub ; chmod 700 ~/.ssh ; chmod 600 ~/.ssh/authorized_keys"
done


