# Awesome deep learning projects
A curated list of deep learning resource and projects inspired by @sindresorhus' [awesome](https://github.com/sindresorhus/awesome) and @veggiemonk's [awesome-docker](https://github.com/veggiemonk/awesome-docker). The primary source of the collection is from [fast.ai](http://course.fast.ai/), a spectacular deep learning course for created by Jeremy Howard and Rachel Thompson.

# Table of Content
- [Image synthesis](#image-sythesis)
  * [CNN](#cnn)
  * [neural style transfer](#neural-style-transfer)
  * [GANs](#gans)
  * [WGANs](#wgans)
  * [AI research](#ai-research)
  * [Neural network approaches for NLP / NLU / dialog / chatbots](#neural-network-approaches-for-nlp-nlu-dialog-chatbots)
  * [General News](#general-news)
  * [Search Interest](#search-interest)
  * [basic](#basic)

## CNN
- [vgg16 model summary](https://s3-us-west-2.amazonaws.com/temptosync/VGG16.png)
- [deep learning basic summary](https://github.com/rodgzilla/Deep-learning-presentation/blob/master/slides_dl.pdf)

## image sythesis
### neural style transfer
- [curating fastai experiments](http://forums.fast.ai/t/curating-lesson-8-experiments/1783)
- [tiling texture images](http://forums.fast.ai/t/tiling-texture-images/1865)
- [Neural Style Transfer & Neural Doodles](https://github.com/titu1994/Neural-Style-Transfer)
- [An implementation of neural style transfer](https://github.com/MatthewKleinsmith/fast-ai-MOOC/blob/master/neural-style-AR.ipynb)
- [blurify to avoid local optimization](https://github.com/aizvorski/fastai-2-work/blob/master/neural-style-better-optimizer.ipynb)
- [experiment starting point neural-style-initialization]( https://gist.github.com/aizvorski/6dee41c61376200014b92ef48480ab15)  
- [experiment with different optimizer](https://medium.com/slavv/picking-an-optimizer-for-style-transfer-86e7b8cba84b#.k91dey4is)
- [an implementation of optimizer experiment](https://github.com/slavivanov/Style-Tranfer)
- [Combining Markov Random Fields and Convolutional Neural Networks for Image Synthesis](https://github.com/chuanli11/CNNMRF)

### GANs
- [an intuitive understanding of GANs](https://hackernoon.com/how-do-gans-intuitively-work-2dda07f247a1#.lp1edlkay)
- [GANs in 50 lines](https://medium.com/@devnag/generative-adversarial-networks-gans-in-50-lines-of-code-pytorch-e81b79659e3f#.gtwdau6fg)
- [GANs in 50 lines implementation](https://github.com/devnag/pytorch-generative-adversarial-networks)
- [Generative Adversarial Text to Image Synthesis](https://arxiv.org/pdf/1605.05396.pdf)
- [DCGan](https://github.com/Newmu/dcgan_code)

### WGANs
- [ Wasserstein distance Jupyter notebook](https://github.com/vincentherrmann/wasserstein-notebook/blob/master/Wasserstein_Kantorovich.ipynb)
- [Train a WGAN on the MNIST dataset](https://github.com/bobchennan/keras-contrib/blob/master/examples/mnist_wgan.py)
- [Wasserstein GAN and the Kantorovich-Rubinstein Duality](https://vincentherrmann.github.io/blog/wasserstein/)
- [Read-through: Wasserstein GAN](http://www.alexirpan.com/2017/02/22/wasserstein-gan.html)
- [Wasserstein GAN paper](https://arxiv.org/abs/1701.07875)
- [WGAN1](https://www.facebook.com/groups/675606912596390/permalink/722401081250306/)
- [WGAN2](https://www.facebook.com/groups/675606912596390/permalink/722898947867186/)

### AI research
- [OpenAI paper curation](https://docs.google.com/spreadsheets/d/1xej5Nca2xUUtrZ1GCyPjFMqI9ZgNq_OhgnTxOOMQ2js/edit#gid=404493967)

### Neural network approaches for NLP / NLU / dialog / chatbots
- [discussions with links to papers](http://forums.fast.ai/t/neural-network-approaches-for-nlp-nlu-dialog-chatbots/1802)

### General news
- [abundance 360](http://www.diamandis.com/blog/archive)

### Search Interest
- [GANs visual analogy |google](https://www.google.com/search?q=GANs+visual+analogy&espv=2&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi3iM2r0ePRAhXojVQKHWWYBo0Q_AUICSgC&biw=1277&bih=876#imgrc=Iud-AVyW_9P-oM:)

### Apparel classificaiton
- [apparel classification with style](http://people.ee.ethz.ch/~lbossard/projects/accv12/index.html)
- [rapid cloth retrieval via deep learning and hierachical search](https://www.csie.ntu.edu.tw/~r01944012/icmr15_clothing.pdf)

### Plant village benchmark
- [plantix](http://www.networkedindia.com/2016/10/11/german-startup-peats-plant-disease-app-empowering-indian-farmers/)
- [plantvillage](http://ai.business/2017/01/30/how-artificial-intelligence-and-machine-learning-can-help-farmers-diagnose-crop-diseases/)
- [plant village](https://arxiv.org/pdf/1511.08060v2.pdf)

### My projects
- [crop doctor](https://github.com/xxlatgh/Crop-doctor)
- [crop doctor webapp](http://cropdoctor.herokuapp.com/index)
- [stock ticker picker](http://stock-tickerchart.herokuapp.com/index)

### basic concepts
Important concepts in machine learning, deep learning and math.
- [Deep Learning Glossary](http://wiki.fast.ai/index.php/Deep_Learning_Glossary) - glossary of concepts related to Deep Learning

- [Gradient Descent](http://wiki.fast.ai/index.php/Gradient_Descent) - Gradient descent, stochastic gradient descent (SGD), and optimizing cost functions
- [Log Loss](http://wiki.fast.ai/index.php/Log_Loss) - review of log loss and cross-entropy
- [Linear Algebra for Deep Learning](http://wiki.fast.ai/index.php/Linear_Algebra_for_Deep_Learning) - review of basic Linear Algebra concepts used in Deep Learning.
- [Calculus for Deep Learning](http://wiki.fast.ai/index.php/Calculus_for_Deep_Learning) - review of basic Calculus concepts used in Deep Learning.
- [Mathematical Notation](http://www.rapidtables.com/math/symbols/Basic_Math_Symbols.htm) - primer/cheatsheet on math symbols
- [Linear Regression](http://wiki.fast.ai/index.php/Linear_Regression) - Intro to linear regression with code examples
- [Logistic Regression](http://wiki.fast.ai/index.php/Logistic_Regression) - Intro to logistic regression with code examples
- [Neural Networks](http://wiki.fast.ai/index.php/Neural_Networks) - Intro to neural networks and backpropagation with code examples


### AI talks
- [Rich Sutton 2016](https://www.youtube.com/watch?time_continue=1262&v=pD-FWetbvN8)
