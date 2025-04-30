namespace EditorHtmlWindowsForms;

partial class Form1
{
    /// <summary>
    ///  Required designer variable.
    /// </summary>
    private System.ComponentModel.IContainer components = null;

    /// <summary>
    ///  Clean up any resources being used.
    /// </summary>
    /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
    protected override void Dispose(bool disposing)
    {
        if (disposing && (components != null))
        {
            components.Dispose();
        }
        base.Dispose(disposing);
    }

    #region Windows Form Designer generated code

    /// <summary>
    ///  Required method for Designer support - do not modify
    ///  the contents of this method with the code editor.
    /// </summary>
    private void InitializeComponent()
    {
        label1 = new Label();
        btnLerArquivoBruto = new Button();
        btnLerArquivoProcessado = new Button();
        button3 = new Button();
        btnSair = new Button();
        btnEditar = new Button();
        SuspendLayout();
        // 
        // label1
        // 
        label1.AutoSize = true;
        label1.Font = new Font("Segoe UI", 13.8F, FontStyle.Bold, GraphicsUnit.Point, 0);
        label1.ForeColor = Color.White;
        label1.Location = new Point(290, 84);
        label1.Name = "label1";
        label1.Size = new Size(219, 31);
        label1.TabIndex = 0;
        label1.Text = "O que deseja fazer?";
        // 
        // btnLerArquivoBruto
        // 
        btnLerArquivoBruto.Location = new Point(316, 141);
        btnLerArquivoBruto.Name = "btnLerArquivoBruto";
        btnLerArquivoBruto.Size = new Size(168, 29);
        btnLerArquivoBruto.TabIndex = 1;
        btnLerArquivoBruto.Text = "Ler arquivo bruto";
        btnLerArquivoBruto.UseVisualStyleBackColor = true;
        btnLerArquivoBruto.Click += btnLerArquivoBruto_Click;
        // 
        // btnLerArquivoProcessado
        // 
        btnLerArquivoProcessado.Location = new Point(316, 191);
        btnLerArquivoProcessado.Name = "btnLerArquivoProcessado";
        btnLerArquivoProcessado.Size = new Size(168, 29);
        btnLerArquivoProcessado.TabIndex = 2;
        btnLerArquivoProcessado.Text = "Ler arquivo formatado";
        btnLerArquivoProcessado.UseVisualStyleBackColor = true;
        btnLerArquivoProcessado.Click += btnLerArquivoProcessado_Click;
        // 
        // button3
        // 
        button3.Location = new Point(316, 241);
        button3.Name = "button3";
        button3.Size = new Size(168, 29);
        button3.TabIndex = 3;
        button3.Text = "Escrever arquivo";
        button3.UseVisualStyleBackColor = true;
        button3.Click += button3_Click;
        // 
        // btnSair
        // 
        btnSair.BackColor = Color.Red;
        btnSair.FlatStyle = FlatStyle.Popup;
        btnSair.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point, 0);
        btnSair.ForeColor = Color.White;
        btnSair.Location = new Point(353, 332);
        btnSair.Name = "btnSair";
        btnSair.Size = new Size(94, 29);
        btnSair.TabIndex = 4;
        btnSair.Text = "Sair";
        btnSair.UseVisualStyleBackColor = false;
        btnSair.Click += btnSair_Click;
        // 
        // btnEditar
        // 
        btnEditar.Location = new Point(316, 287);
        btnEditar.Name = "btnEditar";
        btnEditar.Size = new Size(168, 29);
        btnEditar.TabIndex = 5;
        btnEditar.Text = "Editar arquivo";
        btnEditar.UseVisualStyleBackColor = true;
        btnEditar.Click += btnEditar_Click;
        // 
        // Form1
        // 
        AutoScaleDimensions = new SizeF(8F, 20F);
        AutoScaleMode = AutoScaleMode.Font;
        BackColor = SystemColors.ActiveBorder;
        ClientSize = new Size(800, 450);
        Controls.Add(btnEditar);
        Controls.Add(btnSair);
        Controls.Add(button3);
        Controls.Add(btnLerArquivoProcessado);
        Controls.Add(btnLerArquivoBruto);
        Controls.Add(label1);
        Name = "Form1";
        StartPosition = FormStartPosition.CenterScreen;
        Text = "Form1";
        ResumeLayout(false);
        PerformLayout();
    }

    #endregion

    private Label label1;
    private Button btnLerArquivoBruto;
    private Button btnLerArquivoProcessado;
    private Button button3;
    private Button btnSair;
    private Button btnEditar;
}
