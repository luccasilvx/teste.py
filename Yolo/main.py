#Carrega as dependências
import cv2
import time

# cores das classes
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

#classes
class_names = []
with open('c:/Users/Administrator/.vscode/CODIGOS PYTHON/Yolo/coco.names', 'r') as f:
    class_names = [cname.strip() for cname in f.readlines()]

#captura do vídeo
cap = cv2.VideoCapture(0)

#carregando os pesos da rede neural
net = cv2.dnn.readNet("c:/Users/Administrator/.vscode/CODIGOS PYTHON/Yolo/yolov4-tiny.weights", "c:/Users/Administrator/.vscode/CODIGOS PYTHON/Yolo/yolov4-tiny.cfg")

#setando os parametros da rede neural
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255)

#lendo os frames do video
while True:

    #captura do frame
    _, frame = cap.read()

    #começo da contagem dos ms
    start = time.time()

    #detecção
    classes, scores, boxes = model.detect(frame,0.1, 0.2)

    #fim da contagem dos ms
    end = time.time()

    #percorrendo todas detecções
    for (classid, score, box) in zip(classes, scores, boxes):

        #gerando uma cor para classe
        color = COLORS[int(classid) % len(COLORS)]

        #pegando o nome da classe pelo id e o seu de acuracia
        label = f"{class_names[classid]} : {score}"

        #desenho da box de detecção
        cv2.rectangle(frame, box, color, 2)

        #inserindo o nome da classe em cima da box do objeto
        cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    #calculando o tempo que levou para fazer a detecção
    fps_label = f"FPS:{round((1.0/(end - start)),2)}"

    #escrevendo o fps na imagem
    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 5)
    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    #mostrando a imagem
    cv2.imshow("detections", frame)

    #espera da resposta
    if cv2.waitKey(1) == 27:
        break

#liberação da câmera e destroi todas as janelas
cap.release()
cv2.destroyAllWindows()

