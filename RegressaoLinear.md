<style>
    body {
        text-align: justify;
        font-family: "Times new Roman", Times, serif;
    }
</style>

<center> <h1>Regressão Linear Multipla</h1> </center>
<center> <p>Fundamentos Teóricos</p> </center>

A Análise de regressãoé ferramenta estatística para a modelagem de comportamentos que envolvem a relação entre duas ou mais variáveis. Como exemplo podemos considerar a relção existente entre potência elétrica e a velocidade dovento em um aerogerador. A regressão pode também ser utilizada para otimização de processos,encontrando valores que maximiazam um rendimento.

A regressão busca correlacionar um conjunto de dados e aproximar um modelo probabilístico  que  rege  o  comportamento  da  variável  que  depende  desses  dados. Um dosartifícios para o auxílio da análise do comportamento dos dados, é chamado diagrama de dispersão, um gráfico que mostra a disposição dos dados no eixo, e a correlação, que pode apresentar-se em várias intersidades. É possivel, a partir do gráfico, perceber visualmente, se as variáveis analisadas possuem correlação fraca ou forte.
<hr>

### **Modelo de Regressão Linear Multipla**
Na maioria das situações, os sistemas a serem analisados possuem mais de uma variável regressora.  Um modelo usado para estas situações, que possui mais de uma variável independente é chamado de modelo de regressão multipla.

#### **Equação dos Mínimos Quadrados**
O modelo de regressão múltipla considera $k$ variáveis regressoras e $n$ observações,com $n > k$, que resultam em $n$ equações de regressão $(y_1,y_2,\ldots,y_n)$. A equação de regressão em sua forma matricial $(\textbf{Y})$, que é função $\textbf{X}$ é dada por

$$\textbf{Y} = \textbf{X}\beta + \epsilon.$$

Nessa equação, $\textbf{Y}$ é o vetor de variáveis mensuradas da amostra, $\textbf{X}$ é a matriz de variáveis exploratórias e $\beta$, o vetor de coeficientes de regressão a serem estimados, a partir das variáveis apresentadas na amostra.

$$
\textbf{y} = \begin{bmatrix}
                    y_1\\
                    y_2\\
                    y_3\\
                    \vdots\\
                    y_n
                \end{bmatrix}_{n\times1}

    \textbf{X} = \begin{bmatrix}
                    1 & x_{11} & x_{12} & \ldots & x_{1k}\\
                    1 & x_{21} & x_{22} & \ldots & x_{2k}\\
                    \vdots & \vdots & \vdots & \ddots & \vdots\\
                    1 & x_{n1} & x_{n1} & \ldots & x_{nk}
                \end{bmatrix}_{n\times p}
$$
$$
    \textbf{$\beta$} = \begin{bmatrix}
                            \beta_0\\
                            \beta_1\\
                            \beta_2\\
                            \vdots\\
                            \beta_k
                        \end{bmatrix}_{p\times1} \quad
    \textbf{$\epsilon$} = \begin{bmatrix}
                                \epsilon_1\\
                                \epsilon_2\\
                                \vdots\\
                                \epsilon_n\\
                            \end{bmatrix}_{n\times1}
$$

em que $p=k+1$. Deseja-se encontrar uma equação que minimize a norma quadrática dos vetor de erros $\epsilon$, dado por
$$
\begin{Vmatrix}
    \epsilon^2
\end{Vmatrix} =  \epsilon^T\epsilon = 
    (\textbf{Y}−\textbf{X}β)^T(\textbf{Y}−\textbf{X}β).$$

Derivando essa equação em relação ao vetor $\beta$ e igualando a $\textbf 0$, chegamos à equação do estimador $\hat{\beta}$, os coeficientes de determinação estimados da equação de regressão,

$$
\hat{\beta} = (\textbf{X}^T\textbf{X})^{−1}\textbf{X}^T\textbf{Y}.
$$

Uma vez encontrado o vetor $\beta$, torna-se possível a modelagem da função estimadora de regressão. Dada pela equação matricial seguinte:

$$\textbf{Y}=\textbf{X}\hat\beta$$

O modelo de regressão linear $\textbf{Y}=\textbf{X}\beta + \epsilon$ pode ser ajustado para qualquer sistema que seja linear nos parâmetros $\beta$. Um dos sistemas que pode ser modelado através dessa equação é a classede regressão polinomial. Nesse sistema, as $k$ variáveis independentes se tornam, $x_1,x_2^2,...,x_k^k$. Portanto, é possível obter uma maior precisão na modelagem de comportamentos que sejam não lineares. O gráfico gerado pela equação polinomial obtida é uma curva, que possui uma adequação muito maior aos sistemas do que uma reta.
