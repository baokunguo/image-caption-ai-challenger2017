mlt ensemble.train.txt --name 0,1 -group 0  -c si
mlt ensemble.train.txt --name 0,1 -group 0  -c fss -vl 1
#mlt ensemble.train.txt --name 0,1 -group 0  -cl gbrank -wr 1 -excl model,vote,tfidf --ntree 10 --mil 100 -smooth 0.5 --entropy 0.5 -nbag 10 -nbagfrac 0.8 -nt 10
#mlt ensemble.train.detect_person.txt --name 0,1 -group 0  -cl gbrank -wr 1 -excl model,vote,tfidf -smooth 0.5 --entropy 0.5 -nbag 10 -nbagfrac 0.8 -nt 10 --ntree 20 --nl 32 --lr 0.1 --mil 100
#mlt ensemble.train.detect_person.txt --name 0,1 -group 0  -cl gbrank -wr 1 -excl model,vote,tfidf -smooth 0.5 --entropy 0.5 -nbag 10 -nbagfrac 0.8 -nt 10 -mil 100  -ntree 100 --nl 128 --lr 0.025 
mlt ensemble.train.detect_person.txt --name 0,1 -group 0  -cl gbrank -wr 1 -excl model,vote,tfidf -smooth 0.5 --entropy 0.5 -nt 10 -mil 100  -ntree 500 --nl 128 --lr 0.025 -nbag 10 -nbagfrac 0.8
calc-rank-score.py 
nc aichallenger-evaluate.py ensemble.gbdt.evaluate-inference.txt 