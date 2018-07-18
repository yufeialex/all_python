#!/bin/bash
# hosts: 参数指定机器是属于内部机器, inner代表内部机器, outer代表外部机器
#ansible-playbook init_development_rolized.yaml --limit=10.9.19.205 --tags=sshd --extra-vars "hosts=inner" --ask-pass --ask-vault-pass
#ansible-playbook init_development_rolized.yaml --limit=106.15.42.193  --extra-vars "hosts=outer" --ask-pass --ask-vault-pass
ansible-playbook init_development_rolized.yaml  --extra-vars "hosts=inner" --ask-pass --ask-vault-pass
