using System;
using System.IO;
using System.Windows.Forms;

namespace TextEditorWindowsForms
{
    public partial class Form1: Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnAbrir_Click(object sender, EventArgs e)
        {
            try
            {
                string texto = "";
                using (OpenFileDialog file = new OpenFileDialog())
                {
                    file.Title = "Selecione um arquivo";
                    file.Filter = "Arquivos de texto (*.txt)|*.txt";
                    if (file.ShowDialog() == DialogResult.OK)
                    {
                        using (var reader = new StreamReader(file.FileName))
                        {
                            texto = reader.ReadToEnd();
                            MessageBox.Show(texto,"Conteúdo do arquivo");
                        }
                    }
                }
            }
            catch(Exception ex)
            {
                MessageBox.Show($"Algum erro ocorreu durante a execução do programa : {ex.Message}", "Erro", MessageBoxButtons.OKCancel, MessageBoxIcon.Error);
            }

        }

        private void btnEscrever_Click(object sender, EventArgs e)
        {
            try
            {
                errorProvider1.SetError(txtTextoGravar, string.Empty);
                errorProvider1.SetError(txtNomeArquivo, string.Empty);
                if(string.IsNullOrWhiteSpace(txtTextoGravar.Text))
                {
                    errorProvider1.SetError(btnEscrever, "Para escrever em um arquivo precisa ter um texto válido");
                    return;
                }
                if (string.IsNullOrWhiteSpace(txtNomeArquivo.Text))
                {
                    errorProvider1.SetError(btnEscrever, "Para escrever em um arquivo precisa ter um nome de arquivo válido");
                    return;
                }
                errorProvider1.SetError(txtTextoGravar, string.Empty);
                errorProvider1.SetError(txtNomeArquivo, string.Empty);
                string caminhoPasta = "";
                using(FolderBrowserDialog browser = new FolderBrowserDialog())
                {
                    browser.Description = "Selecione uma pasta para salvar o arquivo";
                    if (browser.ShowDialog() == DialogResult.OK)
                    {
                        caminhoPasta = browser.SelectedPath;
                    }
                }

                using(StreamWriter writer = new StreamWriter($"{caminhoPasta}\\{txtNomeArquivo.Text}.txt"))
                {
                    writer.Write(txtTextoGravar.Text);
                }

                MessageBox.Show($"Arquivo salvo com sucesso em : {caminhoPasta}\\{txtNomeArquivo.Text}.txt","Gravado com sucesso",MessageBoxButtons.OKCancel);

            }
            catch (Exception ex)
            {
                MessageBox.Show($"Algum erro ocorreu durante a execução do programa : {ex.Message}", "Erro", MessageBoxButtons.OKCancel, MessageBoxIcon.Error);
            }
            finally
            {
                txtTextoGravar.Clear();
                txtNomeArquivo.Clear();
            }
        }
    }
}
