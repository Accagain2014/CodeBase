#!/usr/bin/env bash


set_default_var() {
  # Global Const Variables
  AI_HDFS=hdfs**
  AD_HDFS=hdfs**
  GIT_ROOT=`dirname $(readlink -f $0)`
  PROJECT_ROOT=${GIT_ROOT}
  AI_HDFS_HOME=${AI_HDFS}
  AD_HDFS_HOME=${AD_HDFS}/
  ANACONDA=${AI_HDFS_HOME}/anaconda2.tar.gz
  B_LOG_DIR=${GIT_ROOT}/third_party/b-log/
  LOG_DIR=**/log/
  HADOOP=**/bin/hadoop
  SPARK=/usr/bin/hadoop/software/spark/bin/spark-submit

  # Global Config Varaibles
  DATA_DATE=`date +'%Y-%m-%d'`
  FORCE="false"
  STEP_LIST=(
    function
  )
}

print_usage() {
  echo ""
  echo "                                        "
	echo "Options:"
	echo "  -h|--help   This help text."
	echo "  -d|--date   Process data date - default to -2 or -1 day"
	echo "  -f|--force  Force running - true or false, default to false"
	echo "  -s|--step   step to run"
}

parse_args() {
  # Desc:
  #   parse input params from main
  # Param:
  #   $@ from main
  # Return:
  #   None 
  while [[ $# -gt 1 ]]
  do
  local key="$1"
  case $key in
      -h|--help)
        print_usage
        exit 0
      ;;
      -d|--date)
        DATA_DATE="$2"
        shift # past argument
      ;;
      -f|--force)
        FORCE="$2"
        shift
      ;;
      -s|--step)
        STEP_LIST=($2)
        shift 
      ;;
      *)
        echo "Error: Unkown args: ${key}"
        exit 1
      ;;
  esac
  shift # past argument or value
  done
}

init() {
  # Desc:
  # source b-log bash file
  if [[ -f ${B_LOG_DIR}/b-log.sh ]]; then
    source ${B_LOG_DIR}/b-log.sh
    B_LOG --log-level ${LOG_LEVEL_ALL}
    B_LOG --file ${LOG_DIR}/${DATA_DATE}.log --file-prefix-enable --file-suffix-enable
  else
    echo "Error: cannot source b-log.sh"
    exit 1
  fi
  # check ANACONDA
  #if [[ ! -f ${ANACONDA} ]]; then
    #ERROR "Error: no anaconda file at ${ANACONDA}"
    #exit 1
  #fi
}

assert_cmd_success() {
  # Desc:
  #   assert cmd run successfully
  # Param:
  #   $1 -- cmd name
  if [[ $? -ne 0 ]];then
    ERROR "Error: $1 run failed"
    exit 1
  fi
}

assert_hadoop_dir() {
  # Desc:
  #   assert hadoop dir must exist
  # Param:
  #   $1 -- input_dir
  ${HADOOP} fs -test -e $1
  if [[ $? -ne 0 ]];then
    ERROR "Error: hadoop dir not exist (dir: $1)"
    exit 1
  fi
}

function() {
  # Desc:
  # --
  # -- input dir: 
  #
  # -- outpu dir: 
  #
  local output_dir=${AD_HDFS_HOME}/*/
  ${HADOOP} fs -test -e ${output_dir}/_SUCCESS
  if [[ $? -eq 0 && ${FORCE} == "false" ]];then
    INFO "No need to run, output_dir: ${output_dir} is ready"
    return 0
  fi
  local input_dir=${AD_HDFS_HOME}/*/${DATA_DATE}/
  assert_hadoop_dir ${input_dir}
  local job_name="**{DATA_DATE}"
  ${HADOOP} fs -rmr -skipTrash ${output_dir}
  ${HADOOP} streaming \
    -D mapred.job.name="${job_name}" \
    -D mapred.job.maps=500 \
    -D mapred.map.tasks=500 \
    -D mapred.job.reduces=1000 \
    -D mapred.reduce.tasks=1000 \
    -D mapred.job.priority=VERY_HIGH \
    -D mapred.max.map.failures.percent=10 \
    -D mapreduce.user.classpath.first=true \
    -D mapred.textoutputformat.ignore.separator=true \
    -D mapred.ignore.badcompress=true \
    -D mapred.compress.map.output=true \
    -D mapred.child.env="LANG=zh_CN.UTF-8,LC_ALL=zh_CN.UTF-8,PYTHONIOENCODING=UTF-8" \
    -cacheArchive ${ANACONDA}#anaconda2,${AI_HDFS_HOME}wordSegTermWeightModule.zip#wordSegTermWeightModule \
    -file "${PROJECT_ROOT}/python/segment.py" \
    -input ${input_dir} -output ${output_dir} \
    -mapper "anaconda2/bin/python segment.py -seg_col_idx 2"
  assert_cmd_success ${FUNCNAME[0]}
}


#
# Main
#

main() {
  set_default_var
  parse_args $@
  init
  # run all steps
  local step_list_len=${#STEP_LIST[@]}
	for (( i=0; i<${step_list_len}; i++ ))
	do 
    local step=${STEP_LIST[$i]}
    INFO "Step $i: ${step}"
    ${step}
	done
}
# call main function
main $@
