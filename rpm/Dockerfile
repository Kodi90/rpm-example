FROM centos:7

RUN cd /etc/yum.repos.d/ \
    sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-* \
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-* \
    yum update -y \
    yum install -y createrepo rpm-build rpm-sign wget gcc python3 yum-utils tree

#ENV PATH /root/.nimble/bin:$PATH
#RUN curl https://nim-lang.org/choosenim/init.sh -sSf > init.sh
#RUN sh init.sh -y \
#    && choosenim stable
#COPY tools /tools
#RUN cd /tools && \
#    nimble build -Y && \
#    cp -p bin/* /
#
#COPY template.spec /
#COPY entrypoint.sh /usr/local/bin/
#ENTRYPOINT ["entrypoint.sh"]


CMD [ "/bin/bash" ]