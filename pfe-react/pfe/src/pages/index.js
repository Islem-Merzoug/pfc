import React from 'react';
import Card from '../components/Card';
import { models } from '../services/models'; 

const Home = () => {
  console.log(models[0] )
  return (
    <div>
      <Card
          id= { models[0][('id')] }
          name= { models[0][('name')] }
          image= { models[0][('image')] }
          description= { models[0][('description')] }
          detailLink= { models[0][('detailLink')] }
          inputImageExempleLink= { models[0][('inputImageExempleLink')] }
          outputImageExempleLink= { models[0][('outputImageExempleLink')] }
      />

      <Card
          id= { models[1][('id')] }
          name= { models[1][('name')] }
          image= { models[1][('image')] }
          description= { models[1][('description')] }
          detailLink= { models[1][('detailLink')] }
          inputImageExempleLink= { models[1][('inputImageExempleLink')] }
          outputImageExempleLink= { models[1][('outputImageExempleLink')] }
      />


      <div>
        <h1 style={{ display: 'flex', justifyContent: 'center', margin: '30px' }} >Why choose us</h1>

        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '10vh'}} >
          <div class="column" style={{ margin: '15px' }}  >
              Awesome Design
              <div style={{ color: 'gray' }}  > marginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeft </div>
          </div>
          <div class="column" style={{ margin: '15px' }} >
              Notification Update
              <div style={{ color: 'gray' }}  > marginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeft </div>
          </div>
        </div>
        
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '10vh'}} >

          <div class="column" style={{ margin: '15px' }}  >
              Quality AI Models
              <div style={{ color: 'gray' }}  > marginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeft </div>
          </div>
          <div class="column" style={{ margin: '15px' }} >
              Free Bug support
              <div style={{ color: 'gray' }}  > marginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeft </div>
          </div>
          
        </div>
      </div>

      <div>
        <h1 style={{ display: 'flex', justifyContent: 'center', marginTop: '30px' }} >Awesome feachures</h1>

        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '7vh'}} >
        marginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeft marginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeftmarginLeft 
        </div>
      </div>


    </div>
  );
};

export default Home;
