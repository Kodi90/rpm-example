FROM centos:latest

RUN pwd
RUN ls

RUN cd /etc/yum.repos.d/ \
    && sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-* \
    && sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-* \
    && yum update -y \
    && yum install -y createrepo rpm-build rpm-sign wget gcc python3 yum-utils tree

#RUN #rpmdev-setuptree

#RUN #tree

#COPY hello.spec .


CMD [ "/bin/bash" ]