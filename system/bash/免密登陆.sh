# 简易版本, 有时还需修改权限

for ((i=19; i<=34; i++))
do
	scp ~/.ssh/id_rsa.pub sla${i}:~/
	ssh sla${i} "mkdir ~/.ssh; cat ~/id_rsa.pub >> ~/.ssh/authorized_keys ; rm ~/id_rsa.pub"
done


