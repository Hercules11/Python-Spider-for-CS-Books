#### 爬取 名校计算机课程 推荐教材，以及领域内 专家推荐 书籍

网站：https://www.doradolist.com/main.html

**整个项目的流程**：

1. 运行 `books_page.py` 获取推荐书籍的页面链接
2. 运行 `book_info.py` 获取单本书籍的属性信息
3. 运行 `downloader.py` ~~使用 `IP` 代理池，下载书籍~~，目前搞不定，手动下载算了，网站： [Electronic library. Download books free. Finding books (1lib.org)](https://1lib.org/) (网站有多个域名可访问)

------

| 书籍 | 封面 | 推荐次数( >= 10) | 用作 推荐教材 的大学 |
| :----:| :---: | :----: | ------|
| 《[Elements of Information Theory](https://amzn.to/2s6G5oL)》 | <img src="images/Information_Theory_Cover.jpg" width="50%"> | 18 | Stanford, MIT, U of T, Princeton, CMU, EPFL |
| 《[Pattern Recognition and Machine Learning](https://amzn.to/2tqR3rp)》 | <img src="images/Pattern-Recognition-and-Machine-Learning-Christopher-M-Bishop.jpg" width="50%"> | 17 | U of T, Princeton, Harvard, UCLA, USC, Oxford, Cambridge, CMU, EPFL |
| 《[Introduction to Algorithms](https://amzn.to/2GtYILQ)》 | <img src="images/Introduction-to-Algorithms-Thomas-H-Cormen.jpg" width="50%"> | 16 | Stanford, MIT, Berkeley, Caltech, U of T, USC, Oxford, Cambridge, CMU, EPFL |
| 《[The Elements of Statistical Learning](https://amzn.to/2sQZYOK)》 | <img src="images/Statistical-Learning-Hastie.jpg" width="50%"> | 15 | Stanford, MIT, U of T, Princeton, UCLA, USC, Oxford, EPFL |
| 《[Signals and Systems](https://amzn.to/2sfpLTN)》 | <img src="images/Signals-Systems-Oppenheim.jpg" width="50%"> | 13 | Stanford, MIT, Berkeley, Caltech, U of T, Princeton, Oxford, CMU, EPFL |
| 《[Introduction to the Theory of Computation](https://amzn.to/2Hq7Myx)》 | <img src="images/Introduction-to-the-Theory-of-Computation-Michael-Sipser.jpg" width="50%"> | 13 | Stanford, MIT, Berkeley, Caltech, U of T, Harvard, Oxford, Cambridge, CMU, EPFL |
| 《[Speech and Language Processing](https://amzn.to/2stu7q5)》 | <img src="images/Speech-Processing-Jurafsky.jpg" width="50%"> | 11 | Stanford, MIT, U of T, Princeton, USC, Cambridge, EPFL |
| 《[Wireless Communications](https://amzn.to/2seHtGH)》 | <img src="images/Wireless-Communications-Molisch.jpg" width="50%"> | 10 | Stanford, MIT |
| 《[Pattern Classification](https://amzn.to/2rOXgdR)》 | <img src="images/Pattern_Classification_Duda.jpg" width="50%"> | 10 | Stanford, MIT, UCLA, USC |
| 《[Introduction to Probability](https://amzn.to/2r6zQy4)》 | <img src="images/Introduction-to-Probability-Dimitri-P-Bertsekas.jpg" width="50%"> | 10 | Stanford, MIT, Berkeley, U of T, Princeton, UCLA, EPFL |
| 《[Deep Learning](https://amzn.to/2tKqLNd)》 | <img src="images/Deep_Learning_Goodfellow.jpg" width="50%"> | 10 | Stanford, U of T, Princeton, Harvard, Oxford, CMU, EPFL |

完整榜单，[complete_list.md](https://github.com/Hercules11/Python-Spider-for-CS-Books/blob/master/complete_list.md)

注： `*.db` 可用`DB Browser for SQLite` 打开；爬取的书籍仅涉及部分领域；网络不太稳定， `python table.py` 运行了五六次才把图片资源下载好；
