<template>
  <div class="edit-category-container">
    <b-card class="category-card">
    <h1>Update Category - {{ categories.name }}</h1>

    <!-- Form for editing category description and image -->
    <b-form @submit.prevent="submitForm" class="category-form">
      <!-- Category Description (Editable Input) -->
      <b-form-group label="Description:" label-for="desc">
        <b-form-input id="desc" v-model="categories.desc" required></b-form-input>
      </b-form-group>

      <!-- Category Image -->
      <b-form-group label="Image:" label-for="upload_image">
        <b-form-file id="upload_image" name="upload_image" @change="handleImageUpload" required></b-form-file>
      </b-form-group>

      <b-button type="submit" variant="primary" class="submit-button">Submit</b-button>
    </b-form>
  </b-card>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      uploadImage: null,
      categories: {},
    };
  },
  created() {
    this.getCategory();
    document.title='Edit Category';
  },
  methods: {
    handleImageUpload(event) {
      this.uploadImage = event.target.files[0];
    },
    getImageUrl(imageName) {
      return `${imageName}`;
    },
    getCategory() {
      const cat_id = this.$route.params.cat_id;
      const apiurl = `http://127.0.0.1:5000/getCategory/${cat_id}`;
      axios.get(apiurl, {
        headers: {
          Authorization: localStorage.getItem('token')
        }
      })
    .then(response => {
    // Ensure that the 'name' property is correctly assigned
    this.categories = response.data;
  })
      .catch(error => {
        console.error('Error:', error);
      });
    },
    submitForm() {
      const formData = new FormData();
      formData.append('name', this.categories.name);
      formData.append('desc', this.categories.desc);
      formData.append('image', this.uploadImage);

      const cat_id = this.$route.params.cat_id;
      const user = localStorage.getItem('user_type');
      if(user=='storeManager'){
      const apiurl = `http://127.0.0.1:5000/cat_update/${cat_id}`;
      
      axios
      .post(apiurl, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: localStorage.getItem('token')
        },
      })
      .then(() => {
      alert("Updated Category sent for admin approval")
      this.$router.push('/store/category');
    })
      .catch(error => {
        console.error('Error:', error);
      });
    }

    if(user=='admin'){
      const apiurl = `http://127.0.0.1:5000/admin/cat_update/${cat_id}`;
      axios
      .post(apiurl, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: localStorage.getItem('token')
        },
      })
      .then(() => {
      alert("Updated Category")
      this.$router.push('/admin/category');
    })
      .catch(error => {
        console.error('Error:', error);
      });
    }

    },
  },
};
</script>
    
<style scoped>
.edit-category-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
  padding: 100px 20px; /* Adjust padding for smaller screens */
  text-align: center;
  background-image: url("@/assets/dark.jpg");
  background-size: cover;
  background-position: center;
  min-height: 100vh;
}

.category-card{
  width: 50%;
  align-items: center;
}
.category-form {
  margin-top: 20px;
}

.category-form label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.category-form input[type="text"],
.category-form input[type="number"],
.category-form input[type="file"] {
  width: 100%;
  padding: 8px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 14px;
}

.submit-button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
}

.created-category {
  margin-top: 30px;
  text-align: center;
}

.category-details {
  margin-bottom: 15px;
}

.category-image-container {
  max-width: 300px;
  margin: 0 auto;
}

.category-image {
  max-width: 100%;
  height: auto;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-top: 10px;
}

.go-back-button {
  margin-top: 20px;
}
</style>



