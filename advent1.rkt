(define (how-many-larger loc)
  (local [(define (larger/acc prev cur loc count)
            (cond [(empty? (rest loc)) count]
                  [(cons? (rest loc)) (if (> cur prev)
                                          (larger/acc cur (second loc) (rest loc) (add1 count))
                                          (larger/acc cur (second loc) (rest loc)  count))]))]
    (larger/acc (first loc) (second loc) (rest loc) 0)))

(how-many-larger calcs)

; did the second part in google sheets
