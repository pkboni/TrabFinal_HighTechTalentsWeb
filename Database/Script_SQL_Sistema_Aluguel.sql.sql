CREATE TABLE "Cliente"(
    "id" INTEGER NOT NULL,
    "nome" INTEGER NOT NULL,
    "endereco" INTEGER NOT NULL,
    "data_nascimento" DATE NOT NULL,
    "genero" CHAR(255) NOT NULL,
    "documento" VARCHAR(255) NOT NULL,
    "idtipodocumento" INTEGER NOT NULL
);
ALTER TABLE
    "Cliente" ADD PRIMARY KEY("id");
CREATE TABLE "Aluguel"(
    "id" INTEGER NOT NULL,
    "idcliente" INTEGER NOT NULL,
    "dataaluguel" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "idimovel" INTEGER NOT NULL,
    "idcorretor" INTEGER NOT NULL,
    "idcontrato" INTEGER NOT NULL
);
ALTER TABLE
    "Aluguel" ADD PRIMARY KEY("id");
CREATE TABLE "Corretor"(
    "id" INTEGER NOT NULL,
    "nome" VARCHAR(255) NOT NULL,
    "data_entrada" DATE NOT NULL,
    "genero" CHAR(255) NOT NULL,
    "documento" VARCHAR(255) NOT NULL,
    "idtipodocumento" INTEGER NOT NULL,
    "tempo_empresa" INTEGER NOT NULL,
    "idcargo" INTEGER NOT NULL,
    "data_nascimento" INTEGER NOT NULL
);
ALTER TABLE
    "Corretor" ADD PRIMARY KEY("id");
CREATE TABLE "Imovel"(
    "id" INTEGER NOT NULL,
    "endereco" VARCHAR(255) NOT NULL,
    "idproprietario" INTEGER NOT NULL,
    "idtipo" INTEGER NOT NULL,
    "valor_estimado" DOUBLE PRECISION NOT NULL,
    "idstatusalguelvenda" INTEGER NOT NULL
);
ALTER TABLE
    "Imovel" ADD PRIMARY KEY("id");
CREATE TABLE "Proprietario"(
    "id" INTEGER NOT NULL,
    "nome" VARCHAR(255) NOT NULL,
    "endereco" VARCHAR(255) NOT NULL,
    "genero" CHAR(255) NOT NULL,
    "data_nascimento" DATE NOT NULL,
    "documento" VARCHAR(255) NOT NULL,
    "idtipodocumento" INTEGER NOT NULL
);
ALTER TABLE
    "Proprietario" ADD PRIMARY KEY("id");
CREATE TABLE "Contrato"(
    "id" INTEGER NOT NULL,
    "idtipocontrato" INTEGER NOT NULL,
    "valor_mes" DOUBLE PRECISION NOT NULL,
    "valor_ano" DOUBLE PRECISION NOT NULL,
    "quantidade_meses" INTEGER NOT NULL,
    "idtermos" INTEGER NOT NULL
);
ALTER TABLE
    "Contrato" ADD PRIMARY KEY("id");
CREATE TABLE "Termos"(
    "id" INTEGER NOT NULL,
    "data_inclusao" DATE NOT NULL,
    "descricao" TEXT NOT NULL,
    "is_active" BOOLEAN NOT NULL
);
ALTER TABLE
    "Termos" ADD PRIMARY KEY("id");
CREATE TABLE "Telefone"(
    "id" INTEGER NOT NULL,
    "idpessoa" INTEGER NOT NULL,
    "identidade" INTEGER NOT NULL,
    "idtipotelefone" INTEGER NOT NULL,
    "numero_telefone" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Telefone" ADD PRIMARY KEY("id");
CREATE TABLE "TipoTelefone"(
    "id" INTEGER NOT NULL,
    "descricao" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "TipoTelefone" ADD PRIMARY KEY("id");
CREATE TABLE "Entidade"(
    "id" INTEGER NOT NULL,
    "descricao" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Entidade" ADD PRIMARY KEY("id");
CREATE TABLE "AluguelVenda"(
    "id" INTEGER NOT NULL,
    "descricao" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "AluguelVenda" ADD PRIMARY KEY("id");
CREATE TABLE "TipoDocumento"(
    "id" INTEGER NOT NULL,
    "descricao" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "TipoDocumento" ADD PRIMARY KEY("id");
ALTER TABLE
    "Aluguel" ADD CONSTRAINT "aluguel_idcliente_foreign" FOREIGN KEY("idcliente") REFERENCES "Cliente"("id");
ALTER TABLE
    "Aluguel" ADD CONSTRAINT "aluguel_idcorretor_foreign" FOREIGN KEY("idcorretor") REFERENCES "Corretor"("id");
ALTER TABLE
    "Aluguel" ADD CONSTRAINT "aluguel_idimovel_foreign" FOREIGN KEY("idimovel") REFERENCES "Imovel"("id");
ALTER TABLE
    "Imovel" ADD CONSTRAINT "imovel_idproprietario_foreign" FOREIGN KEY("idproprietario") REFERENCES "Proprietario"("id");
ALTER TABLE
    "Proprietario" ADD CONSTRAINT "proprietario_idtipodocumento_foreign" FOREIGN KEY("idtipodocumento") REFERENCES "TipoDocumento"("id");
ALTER TABLE
    "Contrato" ADD CONSTRAINT "contrato_idtermos_foreign" FOREIGN KEY("idtermos") REFERENCES "Termos"("id");
ALTER TABLE
    "Aluguel" ADD CONSTRAINT "aluguel_idcontrato_foreign" FOREIGN KEY("idcontrato") REFERENCES "Contrato"("id");
ALTER TABLE
    "Telefone" ADD CONSTRAINT "telefone_idtipotelefone_foreign" FOREIGN KEY("idtipotelefone") REFERENCES "TipoTelefone"("id");
ALTER TABLE
    "Telefone" ADD CONSTRAINT "telefone_identidade_foreign" FOREIGN KEY("identidade") REFERENCES "Entidade"("id");
ALTER TABLE
    "Imovel" ADD CONSTRAINT "imovel_idstatusalguelvenda_foreign" FOREIGN KEY("idstatusalguelvenda") REFERENCES "AluguelVenda"("id");
ALTER TABLE
    "Cliente" ADD CONSTRAINT "cliente_idtipodocumento_foreign" FOREIGN KEY("idtipodocumento") REFERENCES "TipoDocumento"("id");
ALTER TABLE
    "Corretor" ADD CONSTRAINT "corretor_idtipodocumento_foreign" FOREIGN KEY("idtipodocumento") REFERENCES "TipoDocumento"("id");