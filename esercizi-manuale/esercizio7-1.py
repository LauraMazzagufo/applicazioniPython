# usare l'iterazione al posto della ricorsione nella seguente funzione:
# def stampa_n(s,n):
#     if n <= 0:
#         return
#     print(s)
#     stampa_n(s, n-1)
#
# stampa_n("ciao", 3)
# stampa_n(4, 5)

def stampa_n(s, n):
    while n > 0:
        print(s)
        n = n - 1

stampa_n("ciao", 3)
stampa_n(4, 5)
