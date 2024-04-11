<template>
  <div class="create-category-container">
    <b-card class="category-card">
    <h1>Create Category</h1>
    <b-form @submit.prevent="submitForm" class="category-form">
    <!-- Category Name -->
    <b-form-group label="Category Name:" label-for="name">
      <b-form-input id="name" v-model="name" required></b-form-input>
    </b-form-group>

    <!-- Category Description -->
    <b-form-group label="Description:" label-for="desc">
      <b-form-input id="desc" v-model="desc" required></b-form-input>
    </b-form-group>

    <!-- Category Image -->
    <b-form-group label="Image:" label-for="upload_image">
      <b-form-file
        id="upload_image"
        name="upload_image"
        @change="handleImageUpload"
        required
      ></b-form-file>
    </b-form-group>

    <b-button type="submit" variant="primary" class="submit-button">Submit</b-button>
    <b-button variant="primary" to="/store/category" class="submit-button">Go Back</b-button>
  </b-form>
</b-card>
</div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      desc: '',
      uploadImage: null,
      createdCateg: null,
      user:'',
    };
  },
  created(){
    document.title='Create Category';
  },
  methods: {
    handleImageUpload(event) {
      this.uploadImage = event.target.files[0];
    },
    getImageSrc(imageData) {
            return `data:image/png;base64,${imageData}`
        },
    // getImageUrl(imageName) {
    //   return `${imageName}`;
    // },

    submitForm() {
      this.user = localStorage.getItem('user_type');
      console.log(this.user);

  const formData = new FormData();
  formData.append('name', this.name);
  formData.append('desc', this.desc);
  formData.append('image', this.uploadImage);
  if (this.user=='storeManager'){
  axios
    .post('http://127.0.0.1:5000/cat_create', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        Authorization: localStorage.getItem('token')
      },
    })
    .then(() => {
      alert("New category sent for admin approval")
      this.$router.push('/store/category');
    })
    .catch((error) => {
      console.error(error);
    });
  }

  else if (this.user=='admin'){
  axios
    .post('http://127.0.0.1:5000/admin/cat_create', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        Authorization: localStorage.getItem('token')
      },
    })
    .then(() => {
      alert("Category Created Successfully");
      this.$router.push('/admin/category');
    })
    .catch((error) => {
      console.error(error);
    });
  }
  
},

  },
};
</script>

<style scoped>
.create-category-container {
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
  margin: 10px;
}

.created-category {
  margin-top: 30px;
  text-align: center;
}

.category-details {
  margin-bottom: 15px;
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

.go-back-button {
  margin-top: 20px;
}
</style>

