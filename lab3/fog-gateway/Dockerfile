FROM nodered/node-red:latest
RUN npm install node-red-dashboard
COPY flows.json /data/flows.json
EXPOSE 1880
CMD ["npm", "start", "--", "--userDir", "/data"]