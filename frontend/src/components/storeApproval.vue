<template>
    <div class="categories-container">
      <b-navbar toggleable="lg" type="light" variant="dark" class="gradient-nav">
        <b-navbar-brand  class="navbar-logo">Shopzee</b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
  
        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item class="nav-item"><router-link >Profile</router-link></b-nav-item>
          </b-navbar-nav>
  
          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-button variant="secondary" class="login-button" @click="logout">Logout</b-button>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
        <br>
      <div class="page-container">
      <div v-if="approvals.managers.length > 0">
        <h1>Store Manager Profiles</h1>
            <b-table 
            :items="approvals.managers" 
            bordered 
            head-variant="dark"
            :fields="['name','email', 'approval']">  

                <!-- Name Column -->
                <template v-slot:cell(name)="data">
                    {{ data.value }}
                    </template>

                <!-- Price Column -->
                <template v-slot:cell(email)="data">
                {{ data.value }}
                </template>

                
                <template v-slot:cell(approval)="data">
                <!-- Edit Button -->
                <b-button variant="info" size="sm" @click="approve(1,data.item.id)">
                    Approve 
                </b-button>
                <!-- Delete Button -->
                <b-button variant="danger" size="sm" @click="approve(-1,data.item.id)">
                    Reject
                </b-button>
            </template>
                
        </b-table>
    </div>
      <div v-else>
        <p><b>No Pending Approvals</b></p>
        <b-button variant="primary" to="/admin/dashboard" class="keep-shopping">Go Back</b-button>
      </div>
    </div>
    </div>
  </template>
  
  
  <script>
  import axios from 'axios';
  import {mapActions} from 'vuex'
  
  export default {
    data() {
      return {
        approvals: {},
        code:'',
      };
    },
    mounted() {
      this.getApprovals();
      document.title='Store Manager Approval';
    },
    methods: {
      getApprovals() {
        axios.get('http://127.0.0.1:5000/approval/managers',{
            headers: {
                  Authorization: localStorage.getItem('token'),
              },
            })
          .then((response) => {
            this.approvals = response.data;
            console.log(this.approvals)
          })
          .catch((error) => console.error('error:', error));
          
      },

      approve(code,id){
        const apiurl = 'http://127.0.0.1:5000/approval/managers';
        const formData = new FormData();
        console.log(id);
        console.log(code);
        formData.append('id', id);
        formData.append('code', code);
        axios.post(apiurl, formData,{
        headers: {
            'Content-Type': 'application/json',
            Authorization: localStorage.getItem('token'),
          },
        })
        .then((response)=>{
          alert(response.data.message);
          this.getApprovals();
      })
        .catch((error)=>{
          alert(error);
        })
      },
        ...mapActions({
        signOut: 'LOGOUT_ACTION'
          }),
        logout(){
          this.signOut()
        }
    }
  };
  </script>
  
  <style scoped>
  /* General styles */

  .table-container {
  text-align: center;
}
  .keep-shopping{
    box-align: center; 
    border-radius: 15px; 
    background-color: rgb(10, 110, 85);
    margin: 15px;
  }
  .keep-shopping:hover{
        background-color: white;
        color:#000000;  
  }

  .checkout-button{
    box-align: center; 
    border-radius: 15px; 
    background-color: rgb(219, 89, 89);
  }
  .checkout-button:hover{
        background-color: white;
        color:#000000;  
  }

  .categories-container {
    padding: 0px;
    background-image: url("@/assets/dark.jpg");
    background-size: cover;
    background-position: center;
    min-height: 100vh;
  }
  
  .category-card {
    margin-bottom: 20px;
    padding: 0 50px 0 50px;
  }
  
  .b-card-title {
    font-weight: bold;
  }
  
  .page-container {
  display: flex;
  /* justify-content: center; */
  align-items: center;
  flex-direction: column;  /*Optional: To stack items vertically*/
  min-height: 100vh;
}
  .category-image-container {
    width: 100%; 
    height: 200px; 
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .category-image {
    max-width: 100%;
    max-height: 100%;
  }
  
  .nav-item a{
    color: white;
    text-decoration: none;
  }
  
  .gradient-nav {
    background-image: url("@/assets/card.jpeg");
    background-size: cover;
    background-position: center;
    color: white;
  }
  
  .navbar-logo {
    font-size: 24px;
    font-weight: bold;
  }
  
  .nav-item {
    font-size: 16px;
  }
  
  
  .search-input {
    border-radius: 20px;
    border: none;
    background-color: rgba(255, 255, 255, 0.8);
    padding: 8px 12px;
    color: #333;
  }
  
  .search-button {
    border-radius: 20px;
    margin-left: 10px;
    background-color: #007bff;
    color: white;
    font-weight: bold;
  }
  
  /* Login button styles */
  .login-button {
    border-radius: 20px;
    background-color: #f55;
    color: white;
    font-weight: bold;
  }
  
  .login-button a {
    color: white;
    text-decoration: none;
  }
  
  
  .category-card-inner {
    border: none;
    border-radius: 10px;
    box-shadow: 0px 8px 16px rgb(0, 0, 0);
    background-image: url("@/assets/card.jpeg");
    background-size: cover;
    font-weight: bold;
    background-position: center;
  }
  
  .category-card-text {
    margin: 10px;
    font-size: 18px;
    color: #000000;
  }
  
  .view-products-btn {
    width: 100%;
    margin-top: 10px;
    background-color: #007bff;
  }
  
  .view-products-btn a {
    color: white;
    text-decoration: none;
  }
  

  
  @media screen and (max-width: 767px) {
    .category-card {
      flex: 0 0 100%;
      max-width: 100%;
    }
  }
  </style>