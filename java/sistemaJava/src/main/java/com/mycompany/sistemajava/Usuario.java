/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.sistemajava;

/**
 *
 * @author aluno.den
 */
public class Usuario {

    private String Login;
    private String Senha;
    

 public Usuario (String Login,String Senha){
     
     this.Login=Login;
     this.Senha=Senha;
     
 }
 public String getLogin() {
        return Login;
    }

    public void setLogin(String login) {
        this.Login = login;
    }

    public String getSenha() {
        return Senha;
    }

    public void setSenha(String senha) {
        this.Senha = senha;
    }

}

