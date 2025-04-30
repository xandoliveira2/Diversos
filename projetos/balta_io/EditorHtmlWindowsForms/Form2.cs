namespace EditorHtmlWindowsForms
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        private void btnEscrever_Click(object sender, EventArgs e)
        {
            try
            {
                if (!string.IsNullOrWhiteSpace(txtEscrever.Text) && !string.IsNullOrWhiteSpace(txtNomeArquivo.Text))
                {
                    using (var form = new FolderBrowserDialog())
                    {
                        form.Description = "Selecione uma pasta para salvar seu arquivo";
                        if (form.ShowDialog() == DialogResult.OK)
                        {
                            using (var writer = new StreamWriter(form.SelectedPath + @$"\{txtNomeArquivo.Text}.txt"))
                            {
                                writer.Write(txtEscrever.Text);
                                txtEscrever.Clear();
                                txtNomeArquivo.Clear();
                                MessageBox.Show($"Salvo com sucesso na pasta: {form.SelectedPath}\\{txtNomeArquivo.Text}.txt");

                            }
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Parabéns, você conseguiu causar um erro na aplicação mais simples da sua vida, ta ai sua recompensa {ex.Message}");
            }
        }

        private bool isBetween(int first, int second,int comparison)
        {
            if(first <= comparison && comparison <= second)
            {
                return true;
            }
            return false;
        }
        private void txtNomeArquivo_KeyPress(object sender, KeyPressEventArgs e)
        {
            //48-57 65- 90  97 - 122
            if (!isBetween(48, 57, e.KeyChar) && !isBetween(65, 90, e.KeyChar) && !isBetween(97, 122, e.KeyChar))
                e.Handled = true;
                
            
        }
    }
}
