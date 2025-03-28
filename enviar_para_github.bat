@echo off
cls
echo ---------------------------------------------
echo      ATUALIZANDO PROJETO NO GITHUB
echo ---------------------------------------------

:: Caminho do projeto
cd /d "D:\Python - Códigos\Relatorio Semanal"

:: Mostra o status
echo.
git status

:: Adiciona todas as alterações
echo.
echo Adicionando arquivos...
git add .

:: Pede a mensagem de commit
echo.
set /p mensagem=Digite a mensagem do commit: 

:: Faz o commit com a mensagem digitada
git commit -m "%mensagem%"

:: Envia para o GitHub
echo.
echo Enviando para o GitHub...
git push

echo.
echo ---------------------------------------------
echo      Tudo pronto! Verifique no GitHub. 
echo ---------------------------------------------
pause
