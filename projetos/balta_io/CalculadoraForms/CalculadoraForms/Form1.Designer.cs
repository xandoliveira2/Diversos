namespace CalculadoraForms
{
    partial class Form1
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
            this.visor = new System.Windows.Forms.Label();
            this.subtrair = new System.Windows.Forms.Button();
            this.potencia = new System.Windows.Forms.Button();
            this.divisao = new System.Windows.Forms.Button();
            this.multiplicacao = new System.Windows.Forms.Button();
            this.somar = new System.Windows.Forms.Button();
            this.raiz = new System.Windows.Forms.Button();
            this.um = new System.Windows.Forms.Button();
            this.dois = new System.Windows.Forms.Button();
            this.tres = new System.Windows.Forms.Button();
            this.quatro = new System.Windows.Forms.Button();
            this.cinco = new System.Windows.Forms.Button();
            this.sete = new System.Windows.Forms.Button();
            this.seis = new System.Windows.Forms.Button();
            this.oito = new System.Windows.Forms.Button();
            this.nove = new System.Windows.Forms.Button();
            this.zero = new System.Windows.Forms.Button();
            this.igual = new System.Windows.Forms.Button();
            this.ponto = new System.Windows.Forms.Button();
            this.limpar = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // visor
            // 
            this.visor.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F);
            this.visor.Location = new System.Drawing.Point(35, 24);
            this.visor.Name = "visor";
            this.visor.Size = new System.Drawing.Size(306, 43);
            this.visor.TabIndex = 0;
            this.visor.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // subtrair
            // 
            this.subtrair.Font = new System.Drawing.Font("Microsoft Sans Serif", 20F);
            this.subtrair.Location = new System.Drawing.Point(112, 117);
            this.subtrair.Name = "subtrair";
            this.subtrair.Size = new System.Drawing.Size(74, 46);
            this.subtrair.TabIndex = 2;
            this.subtrair.Text = "-";
            this.subtrair.TextAlign = System.Drawing.ContentAlignment.TopCenter;
            this.subtrair.UseVisualStyleBackColor = true;
            this.subtrair.Click += new System.EventHandler(this.subtrair_Click);
            // 
            // potencia
            // 
            this.potencia.Font = new System.Drawing.Font("Microsoft Sans Serif", 15F);
            this.potencia.Location = new System.Drawing.Point(272, 117);
            this.potencia.Name = "potencia";
            this.potencia.Size = new System.Drawing.Size(74, 46);
            this.potencia.TabIndex = 3;
            this.potencia.Text = "^";
            this.potencia.UseVisualStyleBackColor = true;
            this.potencia.Click += new System.EventHandler(this.potencia_Click);
            // 
            // divisao
            // 
            this.divisao.Location = new System.Drawing.Point(272, 169);
            this.divisao.Name = "divisao";
            this.divisao.Size = new System.Drawing.Size(74, 46);
            this.divisao.TabIndex = 4;
            this.divisao.Text = "/";
            this.divisao.UseVisualStyleBackColor = true;
            this.divisao.Click += new System.EventHandler(this.divisao_Click);
            // 
            // multiplicacao
            // 
            this.multiplicacao.Font = new System.Drawing.Font("Microsoft Sans Serif", 16F);
            this.multiplicacao.Location = new System.Drawing.Point(272, 221);
            this.multiplicacao.Name = "multiplicacao";
            this.multiplicacao.Size = new System.Drawing.Size(74, 46);
            this.multiplicacao.TabIndex = 5;
            this.multiplicacao.Text = "*";
            this.multiplicacao.UseVisualStyleBackColor = true;
            this.multiplicacao.Click += new System.EventHandler(this.multiplicacao_Click);
            // 
            // somar
            // 
            this.somar.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F);
            this.somar.Location = new System.Drawing.Point(32, 117);
            this.somar.Name = "somar";
            this.somar.Size = new System.Drawing.Size(74, 46);
            this.somar.TabIndex = 6;
            this.somar.Text = "+";
            this.somar.UseVisualStyleBackColor = true;
            this.somar.Click += new System.EventHandler(this.somar_Click);
            // 
            // raiz
            // 
            this.raiz.Font = new System.Drawing.Font("Microsoft Sans Serif", 15F);
            this.raiz.Location = new System.Drawing.Point(192, 117);
            this.raiz.Name = "raiz";
            this.raiz.Size = new System.Drawing.Size(74, 46);
            this.raiz.TabIndex = 7;
            this.raiz.Text = "√";
            this.raiz.UseVisualStyleBackColor = true;
            this.raiz.Click += new System.EventHandler(this.raiz_Click);
            // 
            // um
            // 
            this.um.Location = new System.Drawing.Point(32, 169);
            this.um.Name = "um";
            this.um.Size = new System.Drawing.Size(74, 46);
            this.um.TabIndex = 8;
            this.um.Text = "1";
            this.um.UseVisualStyleBackColor = true;
            this.um.Click += new System.EventHandler(this.um_Click);
            // 
            // dois
            // 
            this.dois.Location = new System.Drawing.Point(112, 169);
            this.dois.Name = "dois";
            this.dois.Size = new System.Drawing.Size(74, 46);
            this.dois.TabIndex = 9;
            this.dois.Text = "2";
            this.dois.UseVisualStyleBackColor = true;
            this.dois.Click += new System.EventHandler(this.dois_Click);
            // 
            // tres
            // 
            this.tres.Location = new System.Drawing.Point(192, 169);
            this.tres.Name = "tres";
            this.tres.Size = new System.Drawing.Size(74, 46);
            this.tres.TabIndex = 10;
            this.tres.Text = "3";
            this.tres.UseVisualStyleBackColor = true;
            this.tres.Click += new System.EventHandler(this.tres_Click);
            // 
            // quatro
            // 
            this.quatro.Location = new System.Drawing.Point(32, 221);
            this.quatro.Name = "quatro";
            this.quatro.Size = new System.Drawing.Size(74, 46);
            this.quatro.TabIndex = 11;
            this.quatro.Text = "4";
            this.quatro.UseVisualStyleBackColor = true;
            this.quatro.Click += new System.EventHandler(this.quatro_Click);
            // 
            // cinco
            // 
            this.cinco.Location = new System.Drawing.Point(112, 221);
            this.cinco.Name = "cinco";
            this.cinco.Size = new System.Drawing.Size(74, 46);
            this.cinco.TabIndex = 12;
            this.cinco.Text = "5";
            this.cinco.UseVisualStyleBackColor = true;
            this.cinco.Click += new System.EventHandler(this.cinco_Click);
            // 
            // sete
            // 
            this.sete.Location = new System.Drawing.Point(32, 273);
            this.sete.Name = "sete";
            this.sete.Size = new System.Drawing.Size(74, 46);
            this.sete.TabIndex = 13;
            this.sete.Text = "7";
            this.sete.UseVisualStyleBackColor = true;
            this.sete.Click += new System.EventHandler(this.sete_Click);
            // 
            // seis
            // 
            this.seis.Location = new System.Drawing.Point(192, 221);
            this.seis.Name = "seis";
            this.seis.Size = new System.Drawing.Size(74, 46);
            this.seis.TabIndex = 14;
            this.seis.Text = "6";
            this.seis.UseVisualStyleBackColor = true;
            this.seis.Click += new System.EventHandler(this.seis_Click);
            // 
            // oito
            // 
            this.oito.Location = new System.Drawing.Point(112, 273);
            this.oito.Name = "oito";
            this.oito.Size = new System.Drawing.Size(74, 46);
            this.oito.TabIndex = 15;
            this.oito.Text = "8";
            this.oito.UseVisualStyleBackColor = true;
            this.oito.Click += new System.EventHandler(this.oito_Click);
            // 
            // nove
            // 
            this.nove.Location = new System.Drawing.Point(192, 273);
            this.nove.Name = "nove";
            this.nove.Size = new System.Drawing.Size(74, 46);
            this.nove.TabIndex = 16;
            this.nove.Text = "9";
            this.nove.UseVisualStyleBackColor = true;
            this.nove.Click += new System.EventHandler(this.nove_Click);
            // 
            // zero
            // 
            this.zero.Location = new System.Drawing.Point(32, 325);
            this.zero.Name = "zero";
            this.zero.Size = new System.Drawing.Size(74, 46);
            this.zero.TabIndex = 17;
            this.zero.Text = "0";
            this.zero.UseVisualStyleBackColor = true;
            this.zero.Click += new System.EventHandler(this.zero_Click);
            // 
            // igual
            // 
            this.igual.Font = new System.Drawing.Font("Microsoft Sans Serif", 20F);
            this.igual.Location = new System.Drawing.Point(272, 273);
            this.igual.Name = "igual";
            this.igual.Size = new System.Drawing.Size(74, 95);
            this.igual.TabIndex = 18;
            this.igual.Text = "=";
            this.igual.UseVisualStyleBackColor = true;
            this.igual.Click += new System.EventHandler(this.igual_Click);
            // 
            // ponto
            // 
            this.ponto.Font = new System.Drawing.Font("Microsoft Sans Serif", 20F);
            this.ponto.Location = new System.Drawing.Point(192, 325);
            this.ponto.Name = "ponto";
            this.ponto.Size = new System.Drawing.Size(74, 43);
            this.ponto.TabIndex = 19;
            this.ponto.Text = ".";
            this.ponto.TextAlign = System.Drawing.ContentAlignment.TopCenter;
            this.ponto.UseVisualStyleBackColor = true;
            // 
            // limpar
            // 
            this.limpar.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F);
            this.limpar.Location = new System.Drawing.Point(272, 70);
            this.limpar.Name = "limpar";
            this.limpar.Size = new System.Drawing.Size(74, 46);
            this.limpar.TabIndex = 20;
            this.limpar.Text = "clear";
            this.limpar.UseVisualStyleBackColor = true;
            this.limpar.Click += new System.EventHandler(this.limpar_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(381, 395);
            this.Controls.Add(this.limpar);
            this.Controls.Add(this.ponto);
            this.Controls.Add(this.igual);
            this.Controls.Add(this.zero);
            this.Controls.Add(this.nove);
            this.Controls.Add(this.oito);
            this.Controls.Add(this.seis);
            this.Controls.Add(this.sete);
            this.Controls.Add(this.cinco);
            this.Controls.Add(this.quatro);
            this.Controls.Add(this.tres);
            this.Controls.Add(this.dois);
            this.Controls.Add(this.um);
            this.Controls.Add(this.raiz);
            this.Controls.Add(this.somar);
            this.Controls.Add(this.multiplicacao);
            this.Controls.Add(this.divisao);
            this.Controls.Add(this.potencia);
            this.Controls.Add(this.subtrair);
            this.Controls.Add(this.visor);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Label visor;
        private System.Windows.Forms.Button subtrair;
        private System.Windows.Forms.Button potencia;
        private System.Windows.Forms.Button divisao;
        private System.Windows.Forms.Button multiplicacao;
        private System.Windows.Forms.Button somar;
        private System.Windows.Forms.Button raiz;
        private System.Windows.Forms.Button um;
        private System.Windows.Forms.Button dois;
        private System.Windows.Forms.Button tres;
        private System.Windows.Forms.Button quatro;
        private System.Windows.Forms.Button cinco;
        private System.Windows.Forms.Button sete;
        private System.Windows.Forms.Button seis;
        private System.Windows.Forms.Button oito;
        private System.Windows.Forms.Button nove;
        private System.Windows.Forms.Button zero;
        private System.Windows.Forms.Button igual;
        private System.Windows.Forms.Button ponto;
        private System.Windows.Forms.Button limpar;
    }
}

