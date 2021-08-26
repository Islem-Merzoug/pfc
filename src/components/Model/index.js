import React, {useState} from 'react';
import axios from "axios";
import Loading from '../Loading';

import {
	BrowserRouter as Router,
	Switch,
	Route,
	useHistory,
	useParams
  } from "react-router-dom";
import Popup from "../Popup";
import ReCAPTCHA from "react-google-recaptcha";
import { models } from "../../services/models";

import {
	Btn, BtnInput
} from './ModelElements';

function Model(){
	const [buttonPopup, setButtonPopup] = useState(false)
	const [buttonPopuptwo, setButtonPopuptwo] = useState(false)
	const [selectedFile, setSelectedFile] = useState();
	const [isFilePicked, setIsFilePicked] = useState(false);
	const [isExecuted, setIsExecuted] = useState(false);

	const history = useHistory();

	const changeHandler = (event) => {
		setSelectedFile(event.target.files[0]);
		setIsFilePicked(true);
	};

	const handleConversion = (id) => {
		setIsExecuted(true)

		const formData = new FormData();

		const selectedFileName = selectedFile.name.split('.').slice(0, -1).join('.');

		const selectedFileExtention = selectedFile.name.split('.').pop();
		console.log({
			method  : 'post',
			url : models[id].executeLink,
			data : formData,
		});

		formData.append('file', selectedFile);
		
		axios({
			method  : 'post',
			url : models[id].executeLink,
			data : formData,
		})
		.then((res)=>{
			console.log(res);
			setIsExecuted(false)
			history.push("/stepOne/" + id + "/" + selectedFileName);

		})
		.catch((err) => {
			console.log("err");
			throw err
		});
	}
	
	function onChangeRecapsha(value) {
		console.log("Captcha value:", value);
		setButtonPopup(false)
		setButtonPopuptwo(true)
	  }

	function ModelPost() {
		let { id } = useParams();

		return (

			<div  style={{ padding : '50px 50px'}} >
				<div>
					<h1 style={{ display: 'flex', justifyContent: 'center', marginTop: '30px' }} >{models[id].name}</h1>

					<div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '7vh'}} >
						{models[id].description}
					</div>
				</div>

				<div>
					<div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center'}} >

						<div class="column" style={{ margin: '30px' }} >
							<h1 style={{ display: 'flex', justifyContent: 'left', marginTop: '30px' }} >Input exemple:</h1>

							<img style={{ borderStyle: 'solid', borderColor: 'black' }} src={models[id].inputImageExempleLink} alt='Input exemple' width={400}/>
						</div>

						<div class="column" style={{ margin: '30px' }} >
							<h1 style={{ display: 'flex', justifyContent: 'left', marginTop: '30px' }} >Output exemple:</h1>

							<img style={{ borderStyle: 'solid', borderColor: 'black' }} src={models[id].outputImageExempleLink} alt='Output exemple' width={400}/>
						</div>
					</div>
					
				</div>


				<Popup trigger={ buttonPopup } setTrigger={ setButtonPopup }>
					<ReCAPTCHA
						sitekey="6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
						onChange={onChangeRecapsha}
					/>
				</Popup> 

				<Popup trigger={ buttonPopuptwo } setTrigger={ setButtonPopuptwo }>

					<div>
						<BtnInput type="file" name="file" onChange={changeHandler} />
						{isFilePicked ? (
							<div>
								<div>
									<p>Filename: {selectedFile.name}</p>
									<p>Filetype: {selectedFile.type}</p>
									<p>Size in bytes: {selectedFile.size}</p>
									<p>
										lastModifiedDate:{' '}
										{selectedFile.lastModifiedDate.toLocaleDateString()}
									</p>
									<br/>
									{isExecuted ? (
										<Loading/>
									) : (
										<p>Start the conversion process</p>
									)}

								</div>

								<div>
									<Btn onClick={() => {
										handleConversion(id)

									} 
										}>Convert</Btn>
								</div>
							</div>


						) : (
							<p>Select a file to show details</p>
						)}

					</div>

				</Popup> 

				<Btn type="file" name="file" type="button" onClick={() => setButtonPopup(true) } > Try your own image</Btn>


			
			
			</div>
		)
	}



	return(
		<Router>
			<Switch>
				<Route path="/modelDetails/:id">
					<ModelPost />
				</Route>
			</Switch>
		</Router>

	)
}

export default Model;
