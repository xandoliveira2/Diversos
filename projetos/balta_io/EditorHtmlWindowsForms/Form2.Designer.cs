namespace EditorHtmlWindowsForms
{
    partial class Form2
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            txtEscrever = new TextBox();
            lblnome = new Label();
            txtNomeArquivo = new TextBox();
            btnEscrever = new Button();
            SuspendLayout();
            // 
            // txtEscrever
            // 
            txtEscrever.Location = new Point(26, 79);
            txtEscrever.Multiline = true;
            txtEscrever.Name = "txtEscrever";
            txtEscrever.Size = new Size(749, 359);
            txtEscrever.TabIndex = 0;
            // 
            // lblnome
            // 
            lblnome.AutoSize = true;
            lblnome.Location = new Point(26, 23);
            lblnome.Name = "lblnome";
            lblnome.Size = new Size(104, 20);
            lblnome.TabIndex = 1;
            lblnome.Text = "Nome arquivo";
            // 
            // txtNomeArquivo
            // 
            txtNomeArquivo.Location = new Point(26, 46);
            txtNomeArquivo.Name = "txtNomeArquivo";
            txtNomeArquivo.Size = new Size(125, 27);
            txtNomeArquivo.TabIndex = 2;
            txtNomeArquivo.KeyPress += txtNomeArquivo_KeyPress;
            // 
            // btnEscrever
            // 
            btnEscrever.Location = new Point(157, 44);
            btnEscrever.Name = "btnEscrever";
            btnEscrever.Size = new Size(94, 29);
            btnEscrever.TabIndex = 3;
            btnEscrever.Text = "gravar";
            btnEscrever.UseVisualStyleBackColor = true;
            btnEscrever.Click += btnEscrever_Click;
            // 
            // Form2
            // 
            AutoScaleDimensions = new SizeF(8F, 20F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(btnEscrever);
            Controls.Add(txtNomeArquivo);
            Controls.Add(lblnome);
            Controls.Add(txtEscrever);
            Name = "Form2";
            Text = "Form2";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private TextBox txtEscrever;
        private Label lblnome;
        private TextBox txtNomeArquivo;
        private Button btnEscrever;
    }
}