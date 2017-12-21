#lang racket

(with-output-to-file "module41.out" #:exists 'replace
  (lambda ()
    (let* [(infile (open-input-file "module41.in" #:mode 'text))
           (lines (sort (port->lines infile) string<?))
           (header (format "Total of ~a names" (length lines)))]
      (displayln header)
      (displayln (~a #:min-width (string-length header) #:pad-string "-"))
      (for-each displayln lines))))
