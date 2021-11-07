# ServerPythonProject
Proiect VVS Simplu WebServer in Python
Am facut 2 variante de server , una e async , alta e cu threading
La moment acoperirea am facut cate 11 teste la fiecare din variante .
1.La server cu Threading , am coverage de 50% , in mare parte din cauza unei structuri de date de tip dictionar care nu stiu din ce cauza nu se coloreaza ca executat,
dar se socoate ca ceva ne testat.
a doua problema e testarea socket-ului la orice apelare a testului se primea ca socket.socket fd nu era egal cu cela asteptat si cu asserTrue imi iesea ca la infinit 
se executa testul. Functia principala run() nu stiu cum sa o testez deoarece ea fiind functia unde apelez pe celelalte in ea.
2.La varianta server asincron , am coberage de 53% , in mare parte cauzele ca la varianta cu threading.Varianta server syncron crapa mai des , mai putin persistent.

