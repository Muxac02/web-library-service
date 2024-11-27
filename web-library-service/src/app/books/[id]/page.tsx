import styles from "../../page.module.css";

export default async function BookPage({params}) {
    const paramsResolved = await params

    return (
        <div className={styles.page}>
            <h1>Book page {paramsResolved.id}</h1>
        </div>
    )
}