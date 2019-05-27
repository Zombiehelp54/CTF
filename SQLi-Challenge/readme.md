SQLi Challenge source code. 

The idea is that there is a heavy query being executed in the backend which causes the MySQL server response to be delayed. 
And the server is configured to timeout connections after 10 seconds (50 seconds originally), so there is no way to distinguish
between a subquery that returns true and another that returns false other than causing the mysql server to throw a runtime error.

## Solvers: 
1. @the_st0rm (Ibrahim Mosaad)
2. @ret2got (Jazzy)
3. @terjanq (terjanq)
4. @junorouse (Juno Im)
5. @5unKn0wn (5unKn0wn)
6. @securityidiots (Faraz Khan)
7. @0x4148 (Ahmed Sultan)
8. @pentest_soka (soka)
9. @JosipFranjkovic (Josip Franjkovic)
10. @m_aty (Mohamed Abdel aty)
11. @lnxg33k (Ahmed Shawky)
12. @AmiriusTheThird (Amir Saad) 
13. @Fady_Othman (Fady Othman)

Thanks to everyone who participated.

I will publish a detailed writeup rgarding the original bug and a mod security bypass soon on my blog: http://mahmoudsec.blogspot.com/ 
