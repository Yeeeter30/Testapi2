
export default function handler(req, res) {
    const message = req.query.message || 'Hello, World!';
    res.status(200).json({ message });
}
