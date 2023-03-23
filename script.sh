docker build -t  vn-ecr .
docker tag vn-ecr:latest 445848306891.dkr.ecr.ap-south-1.amazonaws.com/vn-ecr:latest
docker push 445848306891.dkr.ecr.ap-south-1.amazonaws.com/vn-ecr:latest
