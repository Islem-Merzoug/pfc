import React, {useState} from 'react';
import {
	BrowserRouter as Router,
	Switch,
	Route,
	useHistory,
	useParams
  } from "react-router-dom";
import {
	Btn, BtnInput, BtnDownload
} from './StepOneElements';

function StepOne(){

	function BlogPost() {
		let { slug } = useParams();
		return (
			<div style={{ margin : '10px 50px'}}>
					<div >
						<h1 style={{ display: 'flex', justifyContent: 'center', marginTop: '30px' }} >Skin Segmentation</h1>

						<div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '7vh'}} >
						Beginning with a color image, the first stage is to transform it to a skin-likelihood image. This involves transforming every pixel from RGB representation to chroma representation and determining the likelihood value based on the equation given in the previous section. The skin-likelihood image will be a gray-scale image whose gray values represent the likelihood of the pixel belonging to skin. A sample color image and its resulting skin-likelihood image are shown in Figure 3. All skin regions (like the face, the hands and the arms) were shown brighter than the non-skin region. 
						</div>
			</div>
			

			<div style={{ margin : '20px' }}>

				<img 
					style={{   marginLeft: 'auto',
								marginRight: 'auto',
								display: 'block',
								borderStyle: 'solid', 
								borderColor: 'black' }}  
								
					src=" http://localhost:8000/output" alt='Output' />


				<div style={{ textAlign : 'center', padding : '20px'  }} >
					<a style={{ borderStyle: 'solid', borderColor: 'black', padding : '10px' }} href={" http://localhost:8000/output"} download>Download</a>
				</div>
			
			</div>

			</div>
   	);
	  }



	return(

		<Router>
			<Switch>
				<Route path="/;id/fileName">
					<BlogPost />
				</Route>
			</Switch>
		</Router>


	)
}

export default StepOne;