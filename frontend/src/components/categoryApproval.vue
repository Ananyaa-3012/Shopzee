<template>
    <div class="approval-container">
    <b-navbar toggleable="lg" type="light" variant="dark" class="gradient-nav">
        <b-navbar-brand  class="navbar-logo"><router-link to='/admin/dashboard'>Shopzee - Admin</router-link></b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
  
        <b-collapse id="nav-collapse" is-nav>
  
          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-button variant="secondary" class="login-button" size="sm" @click="logout">Logout</b-button>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>

        <br>
  <b-card no-body style="margin-top:20px; margin-right: 40px; margin-left: 40px;">
    <b-card-header header-tag="nav">
      <b-nav card-header tabs>
        <b-nav-item @click="changeTab('create')" :active="activeTab === 'create'" >Create</b-nav-item>
        <b-nav-item @click="changeTab('update')" :active="activeTab === 'update'">Update</b-nav-item>
        <b-nav-item @click="changeTab('delete')" :active="activeTab === 'delete'">Delete</b-nav-item>
      </b-nav>
    </b-card-header>

    <!-- Create Tab Content -->
    <b-card-body class="text-center" v-if="activeTab === 'create'">
      <b-card-title>Created Categories</b-card-title>

  <b-card-text>
    <div v-if="approvals.length>0">
    <b-row>
      <b-col v-for="cat in approvals" :key="cat.id" md="4" class="category-card">
        <b-card 
          :title="cat.name"
          tag="article"
          class="category-card-inner"
        >
        <div class="category-image-container" >
          <img :src="getImageSrc(cat.image)" alt="Category Image" class="category-image" />
        </div>
          
          
          <b-card-text class="category-card-text">
            Description:  {{ cat.desc }}
          </b-card-text>

        <div class="button-row">
          <b-button variant="primary" class="view-products-btn" style="margin-right: 10px;" @click="approve(cat)">
            Approve Category</b-button>
        </div>
            <b-button type="button" variant="danger" @click="showDeleteConfirmation(cat)" style="margin-top: 10px;">
                Reject Category
            </b-button>
         
        </b-card>
      </b-col>
    </b-row>
  </div>
  <div v-else>
    No categories to approve
</div>

</b-card-text>
    </b-card-body>

    <!-- Update Tab Content -->
    <b-card-body class="text-center" v-if="activeTab === 'update'">
      <b-card-title>Updated Categories</b-card-title>

      <b-card-text>
  <div v-if="approvals.length>0">
    <b-row md="2">
      <b-col v-for="cat in approvals" :key="cat.id" md="5" class="category-card">

        <b-card 
          :title="cat.name"
          tag="article"
          class="category-card-inner"
        >
        <b-row >
          <b-col md="6">
            <h3>Old Data</h3>
        <div class="category-image-container" style="margin; 10px">
          <img :src="getImageSrc(cat.image)" alt="Category Image" class="category-image" />
        </div>
        <b-card-text class="category-card-text">
            Description:  {{ cat.desc }}
          </b-card-text>
      </b-col>
      <b-col md="6">
        <h3>New Data</h3>
        <div class="category-image-container" >
          <img :src="getImageSrc(cat.new_image)" alt="Category Image" class="category-image" />
        </div>
        <b-card-text class="category-card-text">
            Description:  {{ cat.new_desc }}
          </b-card-text>
      </b-col>
    </b-row>         
          <div class="button-row">
          <b-button variant="primary" class="view-products-btn" style="margin-right: 10px;" @click="approve(cat)">
            Approve Category</b-button>
        </div>
            <b-button type="button" variant="danger" @click="reject(cat)" style="margin-top: 10px;">
                Reject Category
            </b-button>
        </b-card>
      </b-col>
    </b-row>
  </div>
  <div v-else>
    No categories to approve
</div>

</b-card-text>
    </b-card-body>

    <!-- Delete Tab Content -->
    <b-card-body class="text-center" v-if="activeTab === 'delete'">
      <b-card-title>Created Categories</b-card-title>

  <b-card-text>
    <div v-if="approvals.length>0">
    <b-row>
      <b-col v-for="cat in approvals" :key="cat.id" md="4" class="category-card">
        <b-card 
          :title="cat.name"
          tag="article"
          class="category-card-inner"
        >
        <div class="category-image-container" >
          <img :src="getImageSrc(cat.image)" alt="Category Image" class="category-image" />
        </div>
          
          
          <b-card-text class="category-card-text">
            Description:  {{ cat.desc }}
          </b-card-text>

        <div class="button-row">
          <b-button variant="primary" class="view-products-btn" style="margin-right: 10px;" @click="showDeleteConfirmation(cat)">
            Approve Category</b-button>
        </div>
            <b-button type="button" variant="danger" @click="reject(cat)" style="margin-top: 10px;">
                Reject Category
            </b-button>
         
        </b-card>
      </b-col>
    </b-row>
  </div>
  <div v-else>
    No categories to approve
</div>

</b-card-text>
    </b-card-body>

  </b-card>
</div>

</template>

<script>
  import axios from 'axios';
  import {mapActions} from 'vuex'
  
  export default {
    data() {
      return {
        approvals: {},
        code:0,
        activeTab: 'create'
      };
    },
    mounted() {
      this.getApprovals(this.code);
      console.log(this.approvals);
      document.title='Category Approval'
    },
    methods: {
      getImageSrc(imageData) {
              return `data:image/png;base64,${imageData}`
          },
      getApprovals(cd) {
        axios.get(`http://127.0.0.1:5000/approval/categories?code=${cd}`,{
            headers: {
                  Authorization: localStorage.getItem('token'),
              },
            })
          .then((response) => {
            this.approvals = response.data;
          })
          .catch((error) => console.error('error:', error));
          
      },

      delete(cat){
        const apiurl = `http://127.0.0.1:5000/cat_delete/${cat.id}`;
      axios
        .post(apiurl,{
          headers: {
            'Content-Type': 'application/json',
            Authorization: localStorage.getItem('token'),
          },
        })
        .then(() => {
          alert("Category Deleted Successfully")
          this.getApprovals(this.code);
        })
        .catch((error) => {
          console.error(error);
          // Handle error, e.g., show an error message
        });
      },

      approve(cat){
      // Adjust the endpoint and headers based on your API
      const apiurl = `http://127.0.0.1:5000/approval/category/${cat.id}`;

      axios.post(apiurl, {'code':this.code}, {
        headers: {
          Authorization: localStorage.getItem('token'),
        },
      })
      .then(() => {
        alert("Category Approved");
        this.getApprovals(this.code);
      })
      .catch((error) => {
        console.error(error);
        alert(error);
      });
      },
      reject(cat){
      // Adjust the endpoint and headers based on your API
      const apiurl = `http://127.0.0.1:5000/reject/category/${cat.id}`;

      axios.post(apiurl, {'code':this.code}, {
        headers: {
          Authorization: localStorage.getItem('token'),
        },
      })
      .then(() => {
        alert("Action Rejected");
        this.getApprovals(this.code);
      })
      .catch((error) => {
        console.error(error);
        alert(error);
      });
      },
      showDeleteConfirmation(category) {
        console.log(category);
        const confirmDelete = window.confirm(`Do you want to delete '${category.name}'?`);
        if (confirmDelete) {
          this.delete(category);
        }
      },
      changeTab(tab) {
        this.activeTab = tab;
        if(tab=='create') this.code=0;
        else if (tab=='update') this.code=3;
        else if (tab=='delete') this.code=2;
        this.getApprovals(this.code);
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
   .category-image {
    max-width: 100%;
    max-height: 100%;
  }
  .approval-container{
    background-image: url("@/assets/dark.jpg");
  background-size: cover;
  background-position: center;
  min-height: 100vh;

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

  .login-button {
    border-radius: 20px;
    background-color: #f55;
    color: white;
    font-weight: bold;
  }

  .category-card {
    border: 1px solid #000;
    border-radius: 10px; 
    margin: 10px;
  }
</style>