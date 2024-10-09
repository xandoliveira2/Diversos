// baseado em ECMAscript? não, convenção ecmascript
// babel é o mais famoso compilador de javascript
//******************************************* 
// bundle referencia -> webpack
// bundle = arquivo que contem varios outros arquivos denttro dele, exemplo: um arquivo .js que dentro dele possui varios outros arquivos .js porém pode ter outras extensões 
// compativeis como por exemplo .cjs nesse exemplo, a mesma coisa aconteceria com todos os arquivos do tipo .png por exemplo
// porque é necessário um bundle? para converter em um formato de arquivo que o navegador consiga entender, basicamente ele vai pegar todos arquivos, juntar em um arquivo só,
// e cada arquivo 'pai', serão juntados em um bundle 
// porém isso é algo que não precisa mais se preocupar pois atualmente a maioria dos navegadores (*tirando excessão do internet explorer) possuem suporte para importação de
// modulos
//*******************************************
/* esbuild pode fazer função de compilador e de bundle, porém podemos configurar apenas para compilador, babel é o mais famoso mas não necessáriamente existe só ele, 
aparentemente em uma escala de desempenho, esbuild é um compilador mais rapido, ficando algo nessa ordem:
esbuild - swc - typescript - babel 
basicamente javascript é a base de tudo, usando esbuild, swc ou babel como 'transpiler' (para que seja executado em todas as versões de navegador nesse contexto), já typescript
se refere que ele 'transpila' para o javascript puro
compilar -> alto nivel para baixo nivel ou nivel intermediario de computador
transpilar -> 'alto nivel' para 'alto nivel', mantém o mesmo nivel de abstração, ele transforma o mesmo código em outra linguagem de alto nivel para ser 'traduzido', ou até mesmo
na mesma linguagem só que em versão diferente
*/ 
console.log('por favor aparece :)')