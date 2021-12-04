(define (pos-depth loi)
  (local [(define (pos-depth/acc loi so-far)
            (cond [(empty? loi) so-far]
                  [(cons? loi) (acc/helper loi so-far)]))
          (define (acc/helper loi so-far)
            (local [(define instruction (first loi))
                    (define mag (second loi))
                    (define cur-pos (first so-far))
                    (define cur-dep (second so-far))]
              (cond [(symbol=? instruction 'forward) (pos-depth/acc (rest (rest loi))
                                                                 (list (+ cur-pos mag) cur-dep))]
                    [(symbol=? instruction 'down) (pos-depth/acc (rest (rest loi))
                                                              (list cur-pos (+ cur-dep mag)))]
                    [(symbol=? instruction 'up) (pos-depth/acc (rest (rest loi))
                                                            (list cur-pos (- cur-dep mag)))])))]
    (pos-depth/acc loi (list 0 0))))

(pos-depth instr)

(define test '(forward 5
down 5
forward 8
up 3
down 8
forward 2))

(define (pos-depth2 loi)
    (local [(define (pos-depth/acc loi so-far)
            (cond [(empty? loi) so-far]
                  [(cons? loi) (acc/helper loi so-far)]))
            
          (define (acc/helper loi so-far)
            (local [(define instruction (first loi))
                    (define mag (second loi))
                    (define cur-pos (first so-far))
                    (define cur-dep (second so-far))
                    (define cur-aim (third so-far))]
              (cond [(symbol=? instruction 'forward) (pos-depth/acc (rest (rest loi))
                                                                 (list (+ cur-pos mag) (+ cur-dep (* cur-aim mag)) cur-aim))]
                    [(symbol=? instruction 'down) (pos-depth/acc (rest (rest loi))
                                                              (list cur-pos cur-dep (+ cur-aim mag)))]
                    [(symbol=? instruction 'up) (pos-depth/acc (rest (rest loi))
                                                            (list cur-pos cur-dep (- cur-aim mag)))])))]
    (pos-depth/acc loi (list 0 0 0))))

(pos-depth2 test)
(pos-depth2 instr)