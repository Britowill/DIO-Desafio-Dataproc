#gcloud dataproc clusters create cluster-c91c --region us-central1 --subnet default --zone us-central1-f --master-machine-type n1-standard-4 --master-boot-disk-size 500 --num-workers 3 --worker-machine-type n1-standard-4 --worker-boot-disk-size 500 --image-version 2.0-debian10 --optional-components JUPYTER,ZEPPELIN,ZOOKEEPER --project desafiodataprocdio-329422
#Código para a criação do cluster

with open('resultado_part-00000', encoding="utf8") as file:
    data = file.read().split('\n')
    data = data[:10]
    output = ""
    output = '\n'.join(data)
    print(output)


with open('resultado.txt', 'w') as file:
    file.write(output)