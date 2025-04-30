namespace EditorHtmlWindowsForms
{
    public partial class Form3 : Form
    {
        public Form3()
        {
            InitializeComponent();

        }
        public string caminhoArquivo;

        private void btnSalvar_Click(object sender, EventArgs e)
        {
            try
            {
                if (!string.IsNullOrWhiteSpace(caminhoArquivo))
                {
                 
                    using (var writer = new StreamWriter(caminhoArquivo))
                    {
                        writer.Write(txtEscrever.Text);
                        MessageBox.Show("Salvo com sucesso");
                        this.Close();
                    }
                }
                else MessageBox.Show("Arquivo não encontrado");
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

        }
    }
}
