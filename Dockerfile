FROM adoptopenjdk/openjdk11:alpine-jre
COPY target/*.jar app.jar
ENV SPRING_PROFILES_ACTIVE=ec2
ENV SPRING_CONFIG_NAME=spring-boot-demo
EXPOSE 8090
ENTRYPOINT ["java","-jar","/app.jar"]