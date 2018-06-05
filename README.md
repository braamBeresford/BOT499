# BOT 499


## Step by Step

### 1. File format


### 2. Split the files

<pre>
	./split.sh
</pre>


### 3. Compute Features in Parallel

<pre>
	./submit.sh
</pre>

You can check the status of computation by running:
<pre>
	./check_status.sh
</pre>


### 4. Merge Feature Files
Once the computation has finished, you can merge the feature files.
<pre>
	./merge.sh
</pre>


### 5. 	Feed SVM
And finall you can feed the SVM the feature tables and get an accuracy back
<pre>
	./feed_svm.sh
</pre>


### 6. Clean computed and split files
To remove all the files created through maipulation, not the original data.

<pre>
	./clean.sh
</pre>
