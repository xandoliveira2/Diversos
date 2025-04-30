using System.Runtime.Intrinsics.X86;

namespace EditorHtmlWindowsForms;

public partial class Form1 : Form
{
    public Form1()
    {
        InitializeComponent();

    }

    private void button3_Click(object sender, EventArgs e)
    {
        var frm = new Form2();
        frm.Show();
    }

    private void btnLerArquivoBruto_Click(object sender, EventArgs e)
    {
        try
        {
            using (var file = new OpenFileDialog())
            {
                file.Title = "Selecione um arquivo txt";
                file.Filter = "Selecione um arquivo (*.txt)|*.txt";
                if (file.ShowDialog() == DialogResult.OK)
                {
                    using (var reader = new StreamReader(file.FileName))
                    {
                        using (var frm = new Form3())
                        {
                            frm.txtEscrever.Text = reader.ReadToEnd();
                            frm.txtEscrever.ReadOnly = true;
                            frm.ShowDialog();
                        }

                    }
                }
            }
        }
        catch (Exception ex)
        {
            MessageBox.Show($"Erro!! Essa mensagem eu quero ver: {ex.Message}");
        }

    }

    private void btnSair_Click(object sender, EventArgs e)
    {
        this.Close();
    }

    private void btnLerArquivoProcessado_Click(object sender, EventArgs e)
    {
        try
        {
            using (var file = new OpenFileDialog())
            {
                file.Title = "Selecione um arquivo txt";
                file.Filter = "Selecione um arquivo (*.txt)|*.txt";
                if (file.ShowDialog() == DialogResult.OK)
                {
                    using (var reader = new StreamReader(file.FileName))
                    {
                        using (var frm = new Form4())
                        {
                            processarTexto(reader.ReadToEnd(), frm.txtRichText);
                            frm.ShowDialog();
                        }
                    }
                }
            }
        }
        catch (Exception ex)
        {
            MessageBox.Show($"Erro!! Essa mensagem eu quero ver: {ex.Message}");
        }
    }

    private void processarTexto(string texto, RichTextBox localTexto)
    {
        localTexto.Clear();

        var tagStack = new Stack<FontStyle>();
        int i = 0;

        FontStyle currentStyle = FontStyle.Regular;

        while (i < texto.Length)
        {
            if (texto[i] == '<')
            {
                // Detectar tag de abertura ou fechamento
                int tagEnd = texto.IndexOf('>', i);
                if (tagEnd == -1) break; // Tag malformada, para o parser

                string tag = texto.Substring(i + 1, tagEnd - i - 1).Trim().ToLower(); // Ex: "strong", "/i"
                bool isClosing = tag.StartsWith("/");

                string tagName = isClosing ? tag.Substring(1) : tag;

                // Atualiza estilo com base na tag
                FontStyle tagStyle = tagName switch
                {
                    "strong" => FontStyle.Bold,
                    "i" => FontStyle.Italic,
                    "u" => FontStyle.Underline,
                    _ => FontStyle.Regular
                };

                if (!isClosing)
                {
                    // Abre tag: adiciona estilo
                    tagStack.Push(tagStyle);
                }
                else
                {
                    // Fecha tag: remove a instância correspondente do estilo
                    var tempStack = new Stack<FontStyle>();
                    while (tagStack.Count > 0)
                    {
                        var popped = tagStack.Pop();
                        if (popped == tagStyle) break;
                        tempStack.Push(popped);
                    }
                    // Recoloca o que tirou
                    while (tempStack.Count > 0)
                        tagStack.Push(tempStack.Pop());
                }

                // Atualiza estilo atual
                currentStyle = FontStyle.Regular;
                foreach (var style in tagStack)
                    currentStyle |= style;

                i = tagEnd + 1;
            }
            else
            {
                // Coletar texto normal até a próxima tag
                int nextTag = texto.IndexOf('<', i);
                int length = (nextTag == -1) ? texto.Length - i : nextTag - i;
                string content = texto.Substring(i, length);

                localTexto.SelectionFont = new Font(localTexto.Font, currentStyle);
                localTexto.AppendText(content);
                i += length;
            }
        }
    }

    private void btnEditar_Click(object sender, EventArgs e)
    {
        try
        {
            using (var file = new OpenFileDialog())
            {
                file.Title = "Selecione um arquivo txt";
                file.Filter = "Selecione um arquivo (*.txt)|*.txt";
                if (file.ShowDialog() == DialogResult.OK)
                {
                    using (var frm = new Form3())
                    {
                        using (var reader = new StreamReader(file.FileName))
                        {
                            frm.btnSalvar.Visible = true;
                            frm.caminhoArquivo = file.FileName;
                            frm.txtEscrever.Text = reader.ReadToEnd();
                        }

                        frm.ShowDialog();
                    }
                }
            }
        }
        catch (Exception ex)
        {
            MessageBox.Show($"Erro!! Essa mensagem eu quero ver: {ex.Message}");
        }
    }
}
